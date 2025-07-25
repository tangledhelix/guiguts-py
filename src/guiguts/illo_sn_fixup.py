"""Illustration (Illo) or Sidenote (SN) checking, fixing and tidying functionality"""

import logging
import tkinter as tk
from tkinter import ttk
from typing import Optional, Any

import regex as re

from guiguts.checkers import CheckerDialog
from guiguts.maintext import maintext
from guiguts.misc_tools import tool_save
from guiguts.utilities import IndexRowCol, IndexRange, sound_bell

logger = logging.getLogger(__package__)

_THE_ILLO_CHECKER: Optional["IlloSNChecker"] = None
_THE_SN_CHECKER: Optional["IlloSNChecker"] = None


class IlloSNRecord:
    """Record of Illo or SN in file."""

    def __init__(
        self,
        text: str,
        start: IndexRowCol,
        end: IndexRowCol,
        mid_para: int,
        hilite_start: int,
        hilite_end: int,
    ) -> None:
        """Initialize IlloSNRecord.

        Args:
            text - text of (first line of) the SN or Illo (if caption present).
            start - start rowcol of SN or Illo in file.
            end - end rowcol of SN or Illon in file.
            mid_para - >0 if Illo or SN record mid-para, <0 if previously mid-para, 0 if neither.
            hilite_start - start column of highlighting in text.
            hilite_end - end column of highlighting in text.
        """
        self.text = text
        self.start = start
        self.end = end
        self.mid_para = mid_para
        self.hilite_start = hilite_start
        self.hilite_end = hilite_end


class SelectedIlloSNRecord:
    """Record of start & end line numbers (e.g. '5.0') for selected Illo or SN record"""

    def __init__(self, first: str, last: str) -> None:
        self.first_line_num = first
        self.last_line_num = last


class IlloSNCheckerDialog(CheckerDialog):
    """Illo or Sidenote Checker dialog."""

    def __init__(self, tag_type: str, **kwargs: Any) -> None:
        """Initialize Illo or Sidenote Checker dialog."""

        super().__init__(
            f"{tag_type} Check Results",
            tooltip="\n".join(
                [
                    f"Left click: Select & find {tag_type} tag",
                    "Right click: Hide item",
                    "Shift-Right click: Also hide all matching items",
                ]
            ),
            **kwargs,
        )
        frame = ttk.Frame(self.custom_frame)
        frame.grid(column=0, row=1, sticky="NSEW")
        self.move_up_btn = ttk.Button(
            frame,
            text="Move Selection Up",
            command=lambda: move_selection_up(tag_type),
        )
        self.move_up_btn.grid(column=0, row=0, sticky="NSW")
        self.move_down_btn = ttk.Button(
            frame,
            text="Move Selection Down",
            command=lambda: move_selection_down(tag_type),
        )
        self.move_down_btn.grid(column=1, row=0, sticky="NSW")


class IlloCheckerDialog(IlloSNCheckerDialog):
    """Illustration Fixup dialog."""

    manual_page = "Tools_Menu#Illustration_Fixup"

    def __init__(self, **kwargs: Any) -> None:
        """Initialize Illustration Fixup dialog."""
        super().__init__("Illustration", **kwargs)


class SNCheckerDialog(IlloSNCheckerDialog):
    """Sidenote Fixup dialog."""

    manual_page = "Tools_Menu#Sidenote_Fixup"

    def __init__(self, **kwargs: Any) -> None:
        """Initialize Sidenote Fixup dialog."""
        super().__init__("Sidenote", **kwargs)


class IlloSNChecker:
    """Find, check & record Illos or SNs."""

    def __init__(self, checker_dialog: IlloSNCheckerDialog) -> None:
        """Initialize IlloSNChecker."""
        self.illosn_records: list[IlloSNRecord] = []
        self.checker_dialog: IlloSNCheckerDialog = checker_dialog

    def reset(self) -> None:
        """Reset IlloSNChecker."""
        self.illosn_records = []

    def get_illosn_records(self) -> list[IlloSNRecord]:
        """Return the list of Illo or SN records."""
        return self.illosn_records

    def get_selected_illosn_record(
        self, selected_illosn_index: int
    ) -> SelectedIlloSNRecord:
        """Get line number indexes of the selected Illo or SN record.

        Returns:
            Line number index of first line of the record; e.g. '5.0'
            Line number index of last line of the record; e.g. '6.14'
        """
        # We built a list of Illo or SN records with start/end RowCol details.
        records = self.get_illosn_records()
        # Get record of the selected tag
        selected_record = records[selected_illosn_index]
        selected_record_start = selected_record.start.index()
        selected_record_end = selected_record.end.index()
        rec = SelectedIlloSNRecord(selected_record_start, selected_record_end)
        return rec

    def get_selected_illosn_index(self) -> int:
        """Get the index of the selected Illo or SN record.

        Returns:
            Index into self.illosn_records array, negative if none selected."""
        cur_idx = self.checker_dialog.current_entry_index()
        if cur_idx is None:
            return -1
        text_range = self.checker_dialog.entries[cur_idx].text_range
        assert text_range is not None
        illosn_start = text_range.start
        illosn_records = self.get_illosn_records()
        for illosn_index, illosn_record in enumerate(illosn_records):
            if illosn_record.start == illosn_start:
                return illosn_index
        return -1

    def check_for_anomalous_illo_or_sn(
        self, start: IndexRowCol, end: IndexRowCol
    ) -> bool:
        """Checks for hidden mid-paragraph Sidenotes, and other anomalies.

        The DP Formatting Guidelines allow a Project Manager to request
        that sidenotes are put next to the sentence they apply to in which
        case they are not separated out by blank lines nor prefixed with
        "*". Check for these 'hidden' mid-paragraph sidenotes.

        As a by-product it will also flag as 'MIDPARAGRAPH' other unusual
        formatting of Illo and SN tags in the file.

        Args:
            start - the start RowCol Index of the Illo or SN record.

        Returns:
            True if a 'hidden' mid-paragraph sidenote or other anomaly, False otherwise.
        """
        # An Illo or SN record is normally separated from other file lines by
        # a blank line above and below or one of those blank lines replaced
        # by a Page Marker record. Flag as mid-paragraph any other separation
        # of an Illo or SN record, such as by a blank line on one side and
        # a non-blank line on the other which isn't a Page Marker record.
        #
        file_last_line_num = maintext().end().row
        illosn_first_line_num = start.row
        illosn_last_line_num = end.row
        # Anomalous if line above illo/SN is not blank or page separator (except for first line of file)
        if illosn_first_line_num > 1:
            above_illosn_line_txt = maintext().get(
                f"{illosn_first_line_num - 1}.0", f"{illosn_first_line_num - 1}.end"
            )
            if not (
                above_illosn_line_txt == ""
                or above_illosn_line_txt.startswith("-----File:")
            ):
                return True

        # Find first line below illo/SN that is not blank/[Blank page]/page separator/illo/sidenote
        in_illo_sn = False
        nested = False  # Doesn't handle double nesting
        for line_num in range(illosn_last_line_num + 1, file_last_line_num + 1):
            below_illosn_line_txt = maintext().get(f"{line_num}.0", f"{line_num}.end")
            if (
                below_illosn_line_txt == ""
                or below_illosn_line_txt == "[Blank Page]"
                or below_illosn_line_txt.startswith("-----File:")
            ):
                continue
            # Check if starting illo/SN markup. If on single line, flag is reset below
            if re.match(r"\*?\[(Illustration|Sidenote)", below_illosn_line_txt):
                in_illo_sn = True
            # If in illo/SN, keep on ignoring lines
            if in_illo_sn:
                if "[" in below_illosn_line_txt:
                    nested = True
                # If illo/SN ends, reset the flag
                if "]" in below_illosn_line_txt:
                    if not nested:
                        in_illo_sn = False
                    nested = False
                continue
            # Found "normal" text line - anomalous if previous line is not blank,
            # i.e. not a paragraph start, and ok if previous line is blank
            return maintext().get(f"{line_num - 1}.0", f"{line_num - 1}.end") != ""

        # Hit end of file before finding "normal" text, so not anomalous
        return False

    def run_check(self, tag_type: str) -> None:
        """Run the initial Illustration or Sidenote records check."""
        self.reset()
        search_range = maintext().start_to_end()
        match_regex = (
            r"\[ *illustration" if tag_type == "Illustration" else r"\[ *sidenote"
        )
        # Loop to find all tags of the type specified by argument 'tag_type'.
        # Allow some flexibility in spacing after the opening "[" of the tag.
        while begin_illosn_match := maintext().find_match(
            match_regex, search_range, regexp=True, nocase=True
        ):
            start = begin_illosn_match.rowcol
            # Find colon position, or use end of the required word (i.e. tag_type).
            colon_match = maintext().find_match(
                ":", IndexRange(start, maintext().rowcol(f"{start.row}.end"))
            )
            if colon_match is None:
                colon_pos = maintext().rowcol(
                    f"{start.index()}+{begin_illosn_match.count}c"
                )
            else:
                colon_pos = colon_match.rowcol
            end_point = colon_pos
            # Find closing square bracket - allow open/close bracket within an
            # Illustration or Sidenote record.
            end_match = None
            nested = False
            while True:
                end_match = maintext().find_match(
                    "[][]", IndexRange(end_point, maintext().end()), regexp=True
                )
                if end_match is None:
                    break
                end_point = maintext().rowcol(f"{end_match.rowcol.index()}+1c")
                if maintext().get_match_text(end_match) == "]":
                    if not nested:
                        break  # Found the one we want
                    nested = False  # Closing nesting
                else:
                    if nested:
                        end_match = None  # Not attempting to handle double nesting
                        break
                    nested = True  # Opening nesting

            # If closing [ not found, use end of line.
            if end_match is None:
                end_point = maintext().rowcol(f"{start.row}.end")
            # Get text of (first line of) the Illo or SN line(s) in the file. Note
            # that this does not include any prefixing '*' (that was added by the
            # formatting rounds to show that it is a mid-paragraph tag).
            illosn_txt = maintext().get(f"{start.index()}", f"{start.row}.end")
            # Look for a prefixing '*' to the tag.
            illosn_line = maintext().get(f"{start.index()}-1c", f"{start.row}.end")
            if illosn_line[0:1] == "*":
                mid_para = 1
                illosn_txt = illosn_line
            else:
                # The tag will also be flagged as 'MIDPARAGRAPH' in the dialog if there
                # is any doubt that it is *not* a mid-paragraph tag.
                mid_para = (
                    1 if self.check_for_anomalous_illo_or_sn(start, end_point) else 0
                )
            illosn_rec = IlloSNRecord(
                illosn_txt, start, end_point, mid_para, 1, colon_pos.col - start.col
            )
            self.illosn_records.append(illosn_rec)
            search_range = IndexRange(end_point, maintext().end())

    def update_after_move(
        self, tag_type: str, selected_illosn_index: int, mid_para_list: list[int]
    ) -> None:
        """Update Illo or SN records list, update dialog and reselect tag just moved.

        Args:
            tag_type: either "Illustration" or "Sidenote"
            selected_illosn_index: index of selected illo/sn
            mid_para_list: List of mid-para flags of illos/sns before movement
        """
        # Update illosn_records list
        self.run_check(tag_type)
        # If selected illo/sn was mid-para previous to move(s), and is no longer mid-para,
        # flag it as being "PREV MIDPARA"
        assert len(mid_para_list) == len(self.illosn_records)
        for idx, mid_para_flag in enumerate(mid_para_list):
            if mid_para_flag != 0 and self.illosn_records[idx].mid_para == 0:
                self.illosn_records[idx].mid_para = -1
        # Update dialog
        display_illosn_entries(tag_type)
        # Select again the tag we have just moved so it is highlighted.
        self.checker_dialog.select_entry_by_index(selected_illosn_index)

    def delete_illosn_record_from_file(self, selected: SelectedIlloSNRecord) -> None:
        """Delete the selected Illo/SN record from its original location in the file.

        Do this from the start of (its first) line so that any prefixing '*' is
        included in the deletion. There are 3 cases to consider:
        1. The tag is immediately above a bottom of page Page Marker. Delete the
        tag line(s) and the preceding blank line.
        2. The tag is immediately below a bottom of page Page Marker. Delete the
        tag line(s) and the following blank line.
        3. The tag is mid-page so preceded and followed by a blank line. Delete
        the tag line(s) and the following blank line but leave the preceding
        one.
        """
        # Use marks to get updated index for start & end
        first_line_num = self.updated_index(selected.first_line_num)
        last_line_num = self.updated_index(selected.last_line_num)
        # Line before the (first record of the) Illo or SN record.
        prev_line_num = maintext().index(f"{first_line_num}-1l linestart")
        prev_line_txt = maintext().get(prev_line_num, f"{prev_line_num} lineend")
        # Line after the (last record of the) Illo or SN record.
        next_line_num = maintext().index(f"{last_line_num}+1l linestart")
        next_line_txt = maintext().get(next_line_num, f"{next_line_num} lineend")
        # Assume it's a mid-page Illo or SN record unless found otherwise. This is case 3.
        if prev_line_txt != "":
            # Check this line. It's immediately above the (first line of the) Illo or SN record.
            if prev_line_txt[0:10] == "-----File:" and next_line_txt == "":
                # Case 2
                first_delete_line_num = maintext().index(f"{first_line_num} linestart")
                last_delete_line_num = maintext().index(f"{last_line_num}+2l linestart")
                maintext().delete(first_delete_line_num, last_delete_line_num)
                return
        if next_line_txt != "":
            if next_line_txt[:10] == "-----File:" and prev_line_txt == "":
                # Case 1
                first_delete_line_num = maintext().index(
                    f"{first_line_num}-1l linestart"
                )
                last_delete_line_num = maintext().index(f"{last_line_num}+1l linestart")
                maintext().delete(first_delete_line_num, last_delete_line_num)
                return
        if prev_line_txt == "" and next_line_txt == "":
            # Case 3
            first_delete_line_num = maintext().index(f"{first_line_num} linestart")
            last_delete_line_num = maintext().index(f"{last_line_num}+2l linestart")
            maintext().delete(first_delete_line_num, last_delete_line_num)
            return
        # We get here if anomalous line spacing around the Illo or SN record.
        # Just delete the Illo or SN record and ignore any surrounding lines.
        maintext().delete(
            f"{first_line_num} linestart", f"{last_line_num}+1l linestart"
        )
        return

    def updated_index(self, old_index: str) -> str:
        """Get an updated index using the checker dialog marks.

        If mark doesn't exist for, it's because of a "*" on the first line, so
        we just adjust the index here.

        Args:
            old_index: Old value for index.

        Returns:
            new value for index.
        """
        mark = self.checker_dialog.mark_from_rowcol(IndexRowCol(old_index))
        try:
            new_index = maintext().index(mark)
        except tk.TclError:
            new_index = maintext().index(re.sub(r"\.0$", ".1", mark))
            new_index = re.sub(r"\.1$", ".0", new_index)
        return new_index


def move_selection_up(tag_type: str) -> None:
    """Move selected Illo/SN tag up towards the start of the file.

    We won't move a tag past another tag of the same type.

    Args:
        tag_type: a string which is either "Sidenote" or "Illustration".
    """
    checker = _THE_ILLO_CHECKER if tag_type == "Illustration" else _THE_SN_CHECKER
    assert checker is not None
    selected_illosn_index = checker.get_selected_illosn_index()
    if selected_illosn_index < 0:
        sound_bell()
        return  # No selection.
    # Get the record for the selected tag from the records array we
    # built in run_check().
    selected = checker.get_selected_illosn_record(selected_illosn_index)
    # Group together all inserts/deletes that happen while moving the
    # selected tag.
    maintext().undo_block_begin()
    # Use marks to get updated index for start & end
    first_line_num = checker.updated_index(selected.first_line_num)
    last_line_num = checker.updated_index(selected.last_line_num)
    # Look for a suitable blank line. Start at line immediately above the (first line of
    # the) selected Illo or SN record. NB We may not be able to move the record at all if
    # it means skipping over another tag of the same type.
    line_num = maintext().index(f"{first_line_num}-1l")
    while True:
        # What is on this line?
        line_txt = maintext().get(line_num, f"{line_num} lineend")

        # If closing `]`, find previous `[`
        if line_txt and line_txt[-1] == "]":
            line_num = maintext().search(
                "[", f"{line_num} lineend", 1.0, backwards=True
            )
            if not line_num:  # Hit top of file before tag start
                sound_bell()
                return
            line_num = maintext().index(f"{line_num} linestart")
            line_txt = maintext().get(line_num, f"{line_num} lineend")

        # Is it a tag of the same type as the selected one?
        if tag_type == "Sidenote" and (
            line_txt[0:10] == "[Sidenote:" or line_txt[0:11] == "*[Sidenote:"
        ):
            # Can't move selected Sidenote above another Sidenote.
            sound_bell()
            return
        if tag_type == "Illustration" and (
            line_txt[0:14] == "[Illustration]"
            or line_txt[0:14] == "[Illustration:"
            or line_txt[0:15] == "*[Illustration]"
            or line_txt[0:15] == "*[Illustration:"
        ):
            # Can't move selected Illustration above another Illustration.
            sound_bell()
            return
        # No point in inserting the selected tag above the blank line in the situation below
        # as it will become the same place after the deletion of the Illo or SN record lines
        # from their original position.
        #
        # BL
        # ...
        # BL                     <- blank line we are at.
        # [Sidenote: Some text.] <- (first line of) the selected tag.
        # BL
        # ...
        #
        # If we are not in this situation, insert selected tag above the blank line we are at.
        # Otherwise look for next blank line above that one.
        if line_txt == "" and maintext().compare(
            f"{line_num}+1l linestart", "!=", f"{first_line_num} linestart"
        ):
            # We can insert the selected tag above the blank line at line_num.
            # Copy the lines of the Illo or SN record to be moved. Don't include the
            # prefixing "*" if present.
            the_selected_record_lines = maintext().get(
                first_line_num, f"{last_line_num}"
            )
            if the_selected_record_lines[0:1] == "*":
                the_selected_record_lines = the_selected_record_lines[1:]
            # Delete the selected tag from its current position in the file.
            checker.delete_illosn_record_from_file(selected)
            # Insert copied lines above the blank line we are at and prefix it with a blank line.
            maintext().insert(
                maintext().index(f"{line_num}"),
                "\n" + the_selected_record_lines + "\n",
            )
            mid_para_list = [item.mid_para for item in checker.illosn_records]
            checker.update_after_move(tag_type, selected_illosn_index, mid_para_list)
            break  # Moved successfully
        # If we have reached the top of the file, return.
        if line_num == "1.0":
            sound_bell()
            return
        # Decrement line_num normally.
        line_num = maintext().index(f"{line_num}-1l")
    return


def move_selection_down(tag_type: str) -> None:
    """Move selected Illo/SN tag down towards the end of the file.

    We won't move a tag past another tag of the same type.

    Args:
        tag_type: a string which is either "Sidenote" or "Illustration".
    """
    checker = _THE_ILLO_CHECKER if tag_type == "Illustration" else _THE_SN_CHECKER
    assert checker is not None
    selected_illosn_index = checker.get_selected_illosn_index()
    if selected_illosn_index < 0:
        sound_bell()
        return  # No selection
    # Get the record for the selected tag from the records array we
    # built in run_check().
    selected = checker.get_selected_illosn_record(selected_illosn_index)
    # Group together all inserts/deletes that happen while moving the
    # selected tag.
    maintext().undo_block_begin()
    # Use marks to get updated index for start & end
    first_line_num = checker.updated_index(selected.first_line_num)
    last_line_num = checker.updated_index(selected.last_line_num)
    # Look for a suitable blank line. Start at line immediately below the (last line of
    # the) selected Illo or SN record. NB We may not be able to move the record at all if
    # it means skipping over another tag of the same type.
    line_num = maintext().index(f"{last_line_num}+1l linestart")
    # Set end of loop criteria.
    file_end = maintext().end().index()
    file_end_line_num_plus_1 = maintext().index(f"{file_end}+1l linestart")
    while line_num != file_end_line_num_plus_1:
        # What is on this line?
        line_txt = maintext().get(line_num, f"{line_num} lineend")
        # Is it a tag of the same type as the selected one?
        if tag_type == "Sidenote" and (
            line_txt[0:10] == "[Sidenote:" or line_txt[0:11] == "*[Sidenote:"
        ):
            # Can't move selected Sidenote above another Sidenote.
            sound_bell()
            return
        if tag_type == "Illustration" and (
            line_txt[0:14] == "[Illustration]"
            or line_txt[0:14] == "[Illustration:"
            or line_txt[0:15] == "*[Illustration]"
            or line_txt[0:15] == "*[Illustration:"
        ):
            # Can't move selected Illustration above another Illustration.
            sound_bell()
            return
        # No point in inserting the selected tag below the blank line in the situation below
        # as it will become the same place after the deletion of the Illo or SN record lines
        # from their original position.
        #
        # ...
        # BL
        # [Sidenote: Some text.] <- (last line of) the selected tag.
        # BL                     <- blank line we are at.
        # ...
        # BL
        #
        # If we are not in this situation, insert selected tag below the blank line we are at.
        # Otherwise look for next blank line below that one.
        if line_txt == "" and maintext().compare(
            f"{line_num}-1l linestart", "!=", f"{last_line_num} linestart"
        ):
            # We can insert the selected tag below the blank line at line_num.
            # Copy the lines of the Illo or SN record to be moved. Don't include the
            # prefixing "*" if present.
            the_selected_record_lines = maintext().get(
                first_line_num, f"{last_line_num} lineend"
            )
            if the_selected_record_lines[0:1] == "*":
                the_selected_record_lines = the_selected_record_lines[1:]
            # Insert copied lines below the blank line we are at and suffix it with a blank line.
            maintext().insert(
                maintext().index(f"{line_num} lineend"),
                "\n" + the_selected_record_lines + "\n",
            )
            # Delete the selected tag from its current position in the file.
            checker.delete_illosn_record_from_file(selected)
            mid_para_list = [item.mid_para for item in checker.illosn_records]
            checker.update_after_move(tag_type, selected_illosn_index, mid_para_list)
            return  # Moved successfully
        # Increment line_num.
        line_num = maintext().index(f"{line_num}+1l")
    # Reached end of file without finding a place to move it
    sound_bell()
    return


def illosn_check(tag_type: str) -> None:
    """Check Illustration or Sidenote tags in the currently loaded file.

    Args:
        tag_type: which tag to check for - "Illustration" or "Sidenote"
    """
    global _THE_ILLO_CHECKER
    global _THE_SN_CHECKER

    if not tool_save():
        return
    assert tag_type in ("Illustration", "Sidenote")
    dialog_type = IlloCheckerDialog if tag_type == "Illustration" else SNCheckerDialog
    checker_dialog = dialog_type.show_dialog(
        rerun_command=lambda: illosn_check(tag_type),
        show_suspects_only=True,
        clear_on_undo_redo=True,
    )
    if tag_type == "Illustration":
        if _THE_ILLO_CHECKER is None:
            _THE_ILLO_CHECKER = IlloSNChecker(checker_dialog)
        elif not _THE_ILLO_CHECKER.checker_dialog.winfo_exists():
            _THE_ILLO_CHECKER.checker_dialog = checker_dialog
        the_checker = _THE_ILLO_CHECKER
    else:
        if _THE_SN_CHECKER is None:
            _THE_SN_CHECKER = IlloSNChecker(checker_dialog)
        elif not _THE_SN_CHECKER.checker_dialog.winfo_exists():
            _THE_SN_CHECKER.checker_dialog = checker_dialog
        the_checker = _THE_SN_CHECKER

    the_checker.run_check(tag_type)
    display_illosn_entries(tag_type)
    # Reselect correct entry in case this re-run was after an undo/redo
    checker_dialog.select_entry_after_undo_redo()
    # If that didn't cause anything to be selected, just select the first entry
    if checker_dialog.current_entry_index() is None:
        checker_dialog.select_entry_by_index(0)


def display_illosn_entries(tag_type: str) -> None:
    """(Re-)display the requested Illo/SN tag types in the checker dialog.

    Args:
        tag_type: which tag to check for - "Illustration" or "Sidenote"
    """
    assert tag_type in ("Illustration", "Sidenote")
    the_checker = _THE_ILLO_CHECKER if tag_type == "Illustration" else _THE_SN_CHECKER
    assert the_checker is not None
    checker_dialog = the_checker.checker_dialog
    checker_dialog.reset()
    illosn_records = the_checker.get_illosn_records()
    for illosn_record in illosn_records:
        error_prefix = ""
        if illosn_record.mid_para > 0:
            error_prefix = "MIDPARAGRAPH: "
        elif illosn_record.mid_para < 0:
            error_prefix = "PREV MIDPARA: "
        checker_dialog.add_entry(
            illosn_record.text,
            IndexRange(illosn_record.start, illosn_record.end),
            illosn_record.hilite_start,
            illosn_record.hilite_end,
            error_prefix=error_prefix,
        )
    checker_dialog.display_entries(auto_select_line=False)
