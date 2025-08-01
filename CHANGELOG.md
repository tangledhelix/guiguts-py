# Changelog


## Version 2.0.0

### Bug fixes

- Unicode Block dialog characters were displayed in the wrong font
- Hebrew paste feature always pasted into main text window
- One-line sidenotes were converted incorrectly to HTML
- Png filenames containing hyphens caused a Page Separator Fixup exception
- PPhtml gave incorrect locations for some unused CSS classes
- PPhtml reported multiple links to an id as a failure, not a warning
- Block markup around book title was handled badly by HTML autogeneration
- HTML autogeneration did not add chapter div when block markup preceded
  by 4 blank lines 
- Undoing Replace All from the S/R dialog only worked one change at a time


## Version 2.0.0-beta.3

- Font used for labels, buttons, etc., can now be configured - Mac users
  need to restart Guiguts to see the full benefit
- HTML Links, Anchors and Images can now be added via the HTML menu
- Auto-List added to HTML menu
- Search/Replace dialog can now have up to 10 replacement fields
- Bookmarks now save and restore the current selection
- Replace Match added to Search menu
- Revert/Reload from Disk added to File menu
- CSS classes listed by PPhtml are now sorted
- Fix/Hide All in Basic Fixup now fixes/hides all errors of that type
- Up/Down buttons added to checker dialogs and related commands added to
  Command Palette
- Convert & Find Next button added to Auto-Illustration dialog
- PPtxt has been made significantly less verbose, not reporting several
  things that PPers do not require
- Size grips added to bottom right of checkers and similar dialogs, for
  easier resizing
- Switch Text Window command added to Command Palette
- Recent Files 1, 2 & 3 added to Command Palette
- Delete To End Of Line added to Command Palette
- TIA Abbyy import added to Content Providing menu
- Movement of Illustrations/Sidenotes is now more flexible
- Dutch, Portuguese & Spanish language dictionaries added to release
- Custom commands on Windows that do not use the "start" command will now
  display their results in a command window
- PPtxt no longer reports straight quotes if all quotes are straight
- HTML link checker no longer reports page breaks as unused anchors
- Less strict option for Curly Quote conversion added
- Footnote anchors tied to previous word with Word Joiner character
- Stealth Scanno buttons reorganized for ease of use
- HTML generator uses the dialog's title field to facilitate h1 markup
- HTML generation of chapter headings improved, including dialog option
- Footnote sorting using Alpha/Type has been improved
- Different methods to add words to project/global dictionaries now all
  work the same as one another
- Highlight All highlights are now removed when S/R dialog is closed
- Generated HTML is indented to improve ease of reading
- To reduce cross-platform differences, File-->Exit is named Quit, and
  Preferences is named Settings at the bottom of the Edit menu
- Use of paragraph markup in illustration captions is now optional
- Word Distance entries separated more clearly
- WF Diacritics label clarified
- Curly Quote messages have been shortened for ease of reading
- Checker dialog header layout adjusted to reduce required width
- Unnamed files can no longer be converted to HTML
- If a non-UTF8 file, or one containing a BOM, is loaded, an error is reported
- Installation notes improved and clarified

### Bug fixes

- Deleting a proofer comment could delete a previous fix
- Deleting a proofer comment could leave a double space behind
- Jeebies erroneously reported he/be occurrences that were not lowercase
- HTML autogen used paragraph markup for pagenums within list markup
- Nested square bracket within footnote was not reported, confusing Fixup
- Apply Surround Selection command did not work if dialog was dismissed
- Word Frequency failed to find locations of some "words"
- Word Frequency did not allow some keyboard shortcuts to work
- Pre-existing HTML markup was broken during HTML generation
- Unpaired footnote anchors were not reported
- WF and checkers could cause exception if closed while in progress
- Custom dialog had incorrect example for $s
- Nested footnotes could cause re-indexing problems
- Default command to open a URL did not work on all Linux systems


## Version 2.0.0-beta.2

- Almost all colors used by GG can now be customized by the user via the
  Preferences dialog; colors may be set for the dark theme or light theme
- Alignment options added to Text menu: Center, Right Align, and
  Right Align Numbers
- GG-specific extended regexes added: `\U` uppercases, `\L` lowercases, 
  `\T` titlecases, `\A` creates a hyperlink, `\R` converts to Roman numerals
- GG2 now has the ability to store (using cset) and retrieve (using cget)
  persistent variables when using `\C...\E` to execute python code, similar
  to the use of `lglobal` in GG1
- HTML markup dialog added to HTML menu
- `Convert <sc> Manually` added to Text menu
- Basic Fixup now has View Options so that messages of one type can be
  hidden or shown
- New `Content Providing` submenu of File menu has three functions:
  Export as Prep Text Files, Import Prep Text Files, CP Character Substitution  
- Browse button in image viewer allows user to load any image file
- Scrolling during select-and-drag operations and within image viewer is now
  smoother, particularly on Macs
- In Page Labels configuration dialog, user can now click in the Img and Label
  columns to select the label and jump to the page break in the text file
- Image viewer can now be docked on the left or right of the text window
- View Options dialogs have checkboxes spread evenly across columns
- The busy cursor and "working" label now show during file saving operations
- Spellcheck, Bookloupe and PPtext now ignore page separator lines, ppgen
  command lines, and ppgen comment lines
- Illustration/Sidenote fixups now sound the bell if an attempt is made to
  move an illo/sidenote past another one
- Focus ring around the currently-focused button or other user interface
  control made more visible, especially in dark mode
- Mac installation instructions improved
- Some minor improvments to the wording and case of labels and buttons
- Running `guiguts --version` prints the current Guiguts version number
- New test suite auto-runs some tools and checks the results

### Bug fixes

- Prev/Next Footnote buttons did not work if an anchor line was selected
  in the dialog rather than a footnote line
- HTML autotable sometimes mis-selected the table causing a line to be lost
  or duplicated
- During HTML generation, `<p>` markup was wrongly added around `pagenum`
  spans inside poetry
- Scan images that were stored as palettized or RGB files were never inverted
  in the image viewer
- Illustration Fixup sometimes corrupted Illustration markup when attempting
  to move an illo upwards past an illo block containing blank lines
- HTML generation exited with a fatal error if the file began with `/#` markup
- Mousewheel scrolling in image viewer was broken for Mac users
- PPhtml reported double hyphens in comments in the CSS style block
- PPhtml did not recognize valid DOCTYPE declarations if case was unexpected
- On Linux, Shift-tab did not work correctly to change which user interface
  control had focus
- Some checkboxes in the S/R dialog were wider than needed, so users might
  click them in error, thinking they were clicking in some empty space


## Version 2.0.0-beta.1

- Indent +1/-1/+4 Spaces added to Text menu
- Commonly Used Characters added to Unicode menu - also available using
  Shift+Left-click on status bar character button, with Shift+Right-click
  opening the Unicode Block dialog
- Search/Replace dialog now has "Highlight All" button, which is a more
  powerful version of GG1's "Highlight Char, String & Regex"
- Unicode and Commonly Used Characters display the name of the character
  being hovered overin the dialog, plus a large copy of the character
- Image scroll and zoom commands added to Command Palette so user can
  define keyboard shortcuts
- Tab and Shift+Tab can now be used to navigate to any button or checkbox
  within the main window and all dialogs, to improve accessibility, meaning
  almost everything within Guiguts can be accessed via the keyboard
- Shift+Return operates the Apply button in OK/Apply/Cancel dialogs
- Applying the contents of the "Surround Selection With" dialog is now in
  the Command Palette so can be assigned a keyboard shortcut
- Word Distance Check can now be configured to ignore words with digits
- A few improvements to Stealth Scanno regexes
- Word Frequency navigation resets to start of file after last match is
  found (like GG1); Shift-clicking navigates backwards through
  word occurrences
- Word Frequency Hyphens check, "Two Word" matches are now optional
- PPtxt reports multiple repeated words on one line with just one message
- Proofer comment markup added to "Surround Selection With" Autofill button 
- The Curly Quote check exception to ignore a missing close quote if the
  following paragraph begins with an open quote has been made optional
- When running ebookmaker, user can now control whether they want to create
  EPUB2 files or not
- Small changes to support use of Python 3.13, and README updated to warn
  Mac users about Homebrew-installed Python 3.12 or later
- Touchpad scrolling support for Tk9 added 
- `-p` or `--prefsfile` command line argument can be used to give the basename
  of a preferences file instead of `GGprefs` - for development/testing
- File-save check is omitted in debug mode - for development/testing

### Bug fixes

- User was not warned about using Alt+key as a user-defined shortcut when that
  combination opened a menu on Windows/Linux, e.g. Alt+F for the File menu 
- Bookloupe reported `123.png` as a word containing a digit
- In Word Frequency, clicking on a "word" that began with a non-word character
  but ended with a word character, e.g. `*--the` didn't display the word
- WF reported `Joseph-Marie`, `MacDonald`, `E.g.`, etc. as Mixed Case words
- WF did not ignore ppgen page break commands or comments
- PPhtml failed to spot the charset definition in non-HTML5 files
- Theme queries failed when using Tk9
- OK/Apply buttons in Configure Page Labels did not show whether there were any
  changes to apply
- If Undo/Redo were used from the Edit menu while use Page Separator Fixup, the
  current separator was not re-highlighted
- Adjusting the indent of an ASCII table did not work correctly if the "Rewrap"
  setting was enabled
- Illustration Fixup failed to handle proofer comments inside illo markup
- Bookloupe did not report lower case after period in quotes
- PPtxt did not report a repeated word across a line break in indented text
- PPtxt reported multiple repeated words incorrectly
- PPtxt reported close curly quotes being used as ditto marks as "spaced"
- PPtxt sometimes reported `0` and `1` in decimal numbers as "standalone"
- PPtxt didn't report a potential hyphenated/unhyphenated error if the hyphen
  was at the start or end of the word
- PPhtml reported a cover image over 1MB as an error, not a warning

## Version 2.0.0-alpha.20

### Bug fixes

- Command Palette Edit button gave an exception error message


## Version 2.0.0-alpha.19

- User can define keyboard shortcuts for any menu command as well as several
  other commands that are not in menus. Use Help-->Command Palette, then 
  Edit Shortcut. 
- Ebookmaker can now be run via API without installing it on local computer,
  thus always running latest version installed at PG
- Scan images can now be rotated in the image viewer, with the rotation saved
  permanently per image rotated
- Several improvements to Stealth Scannos: auto-starts immediately; 
  auto-advance checkbox added; search/replace fields are editable; button
  to swap search/replace terms; bad regexes are trapped and reported;
  current and total scanno number displayed; Replace All button fixes all
  issues in the list
- "Surround Selection With" feature added to Edit menu, including autofill
  for closing markup
- Current image name is now displayed in the internal image viewer
- Error messages triggered during file saving are more helpful
- Unmatched Curly Quotes removed due to duplication of features, with its
  unique features added to the Curly Quotes Check
- WF emdash check now includes Unicode emdash characters as well as double
  hyphens, and now ignores intervening punctuation correctly
- PPhtml no longer reports landscape covers with warnings
- Checker dialog no longer forces focus to main window on Windows/Linux

### Bug fixes

- High Contrast label was missing from Preferences dialog
- Page Separator Fixup attempted to join pages with trailing footnotes, but
  failed to do it correctly
- It was not possible to select a leading vertical table line in column 0
- Proofer comment undo also undid user's edits
- WF Hyphen check didn't respect the "case" flag
- Bookloupe wasn't splitting words joined by emdash correctly
- ASCII tables didn't highlight correctly if at top of file
- Closing block markup was sometimes not detected at page breaks
- Superfluous `<br>` and `<p></p>` were sometimes output by HTML generator
- PPgen files were marked as edited when loaded, due to page number commands
- Footnotes were not wrapped when tidied
- Known bugs relating to Tk version 9 have been fixed
- When a bookmark was set/changed, the file was not flagged as needing saving
- Some complex regexes can take a very long time - a timeout now warns the user
- Extending a column selection as the first operation caused an exception


## Version 2.0.0-alpha.18

### Bug fixes

- Cmd/Ctrl-clicking a spell check error removed 2 errors instead of one


## Version 2.0.0-alpha.17

- ASCII Table Effects dialog, similar to GG1, has been added
- HTML Auto-table dialog, similar to section of GG1's HTML Markup dialog,
  has been added
- Backup file now saved when user saves file, with extension `.bak`. Can be
  disabled in Prefs dialog
- Autosave can now be enabled in Prefs dialog, which saves the current file
  every 5 minutes (configurable in Prefs dialog) 
- The Prefs file (where settings are saved) is now backed up so that a "day-"
  and "week-old" version should be retained in the same directory, which can
  be restored if the original becomes corrupted. Now that many settings,
  including Custom menu entries, are saved in the Prefs file, it would be
  more disruptive if Pref file's contents were lost. Procedure: quit Guiguts;
  rename `GGprefs.json` to `GGprefs_corrupt.json`; rename `GGprefs_day.json`
  to `GGprefs.json`; restart Guiguts; if problem not resolved, repeat the
  above, but restoring `GGprefs_week.json`
- Custom Menu added, similar to GG1, but read help in dialog or manual page
  for more details, including how to link to source scans at IA or Hathi Trust
- IMPORTANT note for users upgrading from earlier alpha versions: the location
  of the ebookmaker directory/folder must be re-selected - it is now where
  the `pipenv install ebookmaker` command was run, rather than the ebookmaker
  script in the virtual environment.
- If ebookmaker is installed on user's computer, it can be run from within
  GG on all platforms. Normally runs in verbose mode, but "Verbose" checkbox
  enables further verbosity (mostly for debugging)
- Ebookmaker messages can be sorted by severity; "Suspects only" can be used
  to filter out debug/information messages.
- Command Palette has been added, accessible via the Help menu, or using
  Cmd/Ctrl+Shift+P: it lists all the commands available, and user can type
  part of the command to filter the list, then run the command with the "Run"
  button, or the "Enter/Return" key or double clicking the command. In addition
  to being a feature in its own right, it is intended to use this work to
  support the addition of user-defined shortcut keys in a future release
- Proofer comments can now be deleted, via button or Cmd/Ctrl-clicking in
  Proofer Comments dialog
- Highlighting of current cursor line can be disabled via Prefs dialog
- Display of tooltips can be disabled via Prefs dialog
- End-of-page blank lines, and end-of-line spaces are deleted automatically
  when file is saved
- Pathnames, e.g. scannos filename, are displayed right-aligned in comboboxes
  so the filename is more visible, and a tooltip displays the full pathname
- Link to PPWB is not in Tools menu, and a few button labels have been changed
- Show/Hide Image Viewer menu buttons replaced with Image Viewer checkbox
- All checker dialogs now output "Check complete" at the bottom of the list
- Dialog Manual in the Help menu performs the same task as the F1 key, i.e.
  displays the manual page for the dialog that was most recently used
- When Unicode Search dialog is popped, if there is a character displayed in
  the status bar (i.e. single character selected, or character after cursor)
  the information on that character is displayed

### Bug fixes

- Autoset Chap LZ in Footnote Fixup caused an infinite refreshing loop
- A few PPtxt false positives have been fixed
- PPhtml failed to detect `id="my_id"` when split across a line break
- PPhtml sometimes output a leading comma in the list of defined classes
- PPhtml split classnames containing hyphens into two classes
- HTML & CSS validator dialogs did not link to their manual pages
- Cmd/Ctrl-clicking a spelling error didn't remove it from the list
- Search-->Count, Find All & Replace All with "In selection" checked did not
  work correctly in column selections.
- Line number and column number highlighting foreground color could be wrong
- The CSS validator failed with CSS blocks over 400 lines long
- The current cursor line displayed oddly in combination with split window -
  a known issue is that the cursor line from the other half of the split
  will be displayed (faintly) in the split window
- Footnote reindexing could give incorrect output where multiple footnote
  anchors were on the same line of text
- WF treated underscores as word characters in an inconsistent manner
- Very small image viewer scale factors could cause a traceback


## Version 2.0.0-alpha.16

- The user can now use an external viewer to display scan files, instead of,
  or in addition to, the internal viewer. If the user does not specify a
  particular viewer, the computer's default viewer for PNG files will be used.
  Typically, this is the viewer that would open a PNG file when the operating
  system is asked to "open" or "view" the file, or it is double-clicked when
  using Windows. Alternatively the user can choose a specific viewer, such as
  `XnView` on Windows, `Pixea` on macOS, or `eog -w` on Linux, which will then
  be used instead of the computer's default viewer.
- Help->About Guiguts now reports version numbers and is easier to copy
  when reporting a bug
- A High Contrast preference option increases the contrast of the main text
  window and internal image viewer, i.e. black on white or white on black
- Highlight HTML Tags in the Search menu displays HTML tags in color to make
  it easier to edit HTML files
- Image Viewer now has auto fit-to-height and fit-to-width buttons
- CSS Validator in the HTML menu uses the online W3C validator to validate
  (CSS2.1 or CSS3) and report on the CSS block at the top of the file
- All checker dialogs now have buttons to hide (and fix if appropriate) the
  selected message, instead of requiring use of Cmd/Ctrl with mouse clicks
- The "Default" theme is now dark or light depending on the current operating
  system setting - the user can still choose Dark or Light explicitly
- Clicking (and dragging) in the line numbers on the left now selects whole
  lines of text. Although it is not possible to drag beyond the height of
  the window, large sections of text can be selected by clicking to select
  the first line, scrolling down, then Shift-clicking to select the last
  line. Shift-clicking and dragging extends/reduces the selection in a similar
  way to the behavior in the main text window. The mouse scroll wheel should
  also scroll the text window even when the mouse is in the line numbers
- Checker View Options (e.g. Bookloupe) now mean "show" when checked, rather
  than "hide"
- Checker View Options now have a checkbox to allow the graying out of view
  options that do not match any messages in the checker dialog - in addition
  the number of matching messages is shown next to each view option 
- Curly Quotes now has View Options to allow hide/show of single/double quote
  queries independently
- PPhtml check has been added, based on a combination of the PPWB tool and the
  tool bundled with Guiguts 1 
- A link to the online Post-Processors' Workbench is now in the HTML menu
- The Preferences dialog now has tabs to split the different preferences into
  sections
- A new Advanced tab in the Preferences dialog has settings for line spacing
  which increases the vertical spacing between lines of text, and for cursor
  width which can be increased to make it more visible
- A few small improvements have been made to PPtxt's report
- Spell check does not highlight all the spelling queries in blue
- Ebookmaker check has been added to the HTML menu. Checkboxes determine which
  formats will be created in the project directory. The user must first 
  install ebookmaker according to the instructions here:
  https://github.com/gutenbergtools/ebookmaker/blob/master/README.md
  So far, this has been tested successfully  on Windows, but not on macOS or
  Linux. Feedback would be welcomed.
- An experimental feature to improve the display of Hebrew and Arabic text,
  which is displayed right to left (RTL), attempts to display the text in the
  correct direction. To paste Hebrew text on Windows, or Hebrew and Arabic
  text on Linux, use the new Edit Paste Hebrew/Arabic Text button. This
  reverses the text in a platform appropriate manner, and also adjusts it
  when the file is saved and reloaded. Do not attempt to paste a mixture of
  RTL and LTR text. As with all previous versions of Guiguts 1 and 2, if you
  position the insert cursor within the RTL text, characters may jump around
  unexpectedly, but will be restored when the cursor is moved away. Feedback
  would be welcomed.

### Bug fixes

- Footnote anchors were accidentally included in the autogenerated ToC
- Auto-illustration sometimes failed to spot the end of illo markup
- Sometimes when the window scrolled to show the latest search match, the
  match would be at the very edge of the screen making it hard to spot
- Math fractions like `100/length` were reported by Unmatched Block Markup
- Mac mousewheel/trackpad image scrolling was not smooth


## Version 2.0.0-alpha.15

- HTML Auto Illustrations feature has been added
- Unmatched HTML tag check has been added 
- HTML Validator added using the Nu validator: https://validator.w3.org/nu/
- HTML Link Checker added
- Bookloupe now has a View Options dialog to control which messages are shown
- Image viewer buttons improved, including ability to page through the files
  in the images folder without moving the current text position
- Proofer notes are now optionally highlighted
- A `misspelled.json` stealth scannos file has been added to the release
- Mouse pointer in checker dialogs is now the normal cursor arrow
- Spell Check dialog has shortcut keys using Cmd/Ctrl plus a letter, like GG1:
  A - Add to global dictionary, P - add to Project dictionary, S - Skip,
  I - skIp all
- Search match highlighting speed has been improved
- Previous/next image buttons in the status bar now move to the next image
  even if the text position does not move
- Curly Quote checker reports open quotes preceded by punctuation
- Some Bookloupe false positive reports have been removed, and the wording
  of some messages improved
- Some repeated PPtxt messages removed
- Search dialog shows "No matches found" in addition to sounding the bell
- "Invert Image" has been added to the View menu
- README updated to include changes due to Poetry version 2

### Bug fixes

- Bookloupe could crash when processing a text table using `=` for borders
- Insert cursor wasn't hidden in text split window when a selection was made
- Split text window's column ruler did not always follow the theme color
- Footnotes LZ heading could have 4 blank lines before, but only 1 after  
- Orange spotlights could be left behind when WF or other dialogs closed
- An exception could happen if GG exited while certain dialogs were visible
- Footnotes "Move to paragraphs" could fail due to editing side effect
- HTML Autogen could wrap the book title in both `<h1>` and `<p>` markup


## Version 2.0.0-alpha.14

- When using the Search dialog to search for a string, all occurrences
  of the string are highlighted faintly, in addition to the first occurrence
  being selected as previously. These faint highlights are removes when
  the user begins a new search or closes the Search dialog
- The bookloupe tool has been added. Although it is not identical in 
  behavior to the old external tool, it essentially does the same checks
  and reports issues in a similar way. Most of the differences relate to
  changes in DP/PG texts since the forerunner of bookloupe (gutcheck) was
  first written, such as use of non-ASCII characters.
- When using Save As, GG2 now adds an appropriate extension, which is
  `.txt` unless the file has an HTML header, in which case it is `.html`.
  Also, if there is no filename, Save As suggests `untitled.txt`
- Illo/Sidenote Fixup now automatically select the first message when run
- HTML Autogeneration now reports more specific errors it discovers while
  running, and allows user to re-load the previous backup to fix them

### Bug fixes

- Orange spotlights were hidden when doing Find All within a selection
- Could get warnings if preferences were removed in a previous release
- Asterisk thoughtbreaks were broken by rewrapping
- The first page number in HTML could get inserted before the HTML header
- Swap/delete space functions in curly quote check didn't always work
- Using undo/redo did not cause Sidenote/Illo Fixup to recalculate positions
- The final footnote in the file could cause an error during HTML generation
- HTML Autogeneration didn't show the "busy" cursor to indicate it was working
- HTML Autogeneration didn't consider the last line of the file
- HTML Autogeneration didn't fail gracefully if the final chapter heading did
  not have 2 blank lines after it
- Rapidly cancelling the Search dialog with the Escape key while it was still
  working caused an error to occur


## Version 2.0.0-alpha.13

- HTML Autogeneration has been added. This performs basic conversion to HTML
  in a similar way to GG1. Other features such as image and table conversion
  are not included. To customize the HTML header, the user has two choices.
  The recommended method is to leave the default header as it is in
  `data/html/html_header.txt`, and create a new `html_header.txt` in their
  GGprefs folder which only contains CSS to override or add to the defaults.
  When the HTML file is generated, the default header will be inserted at
  the top of the file, and the user's header will be inserted at the bottom
  of the CSS, just before the closing `</style>` so that the user's CSS
  will override the earlier default settings. This method has the advantage
  that when future releases are made with adjustments to the default header,
  you will not usually need to edit your customized header text.
  The alternative method, which does not have this advantage, is to
  copy the file `html_header.txt` from the `data/html` folder in the
  release into their GGprefs folder and edit it there. That file will be
  used as the complete header for generated HTML files. If the default
  header is altered in a future release, you would need to either copy across
  any new changes into your header, or copy the whole file across and make
  your customizing edits again.
- There is a manual page for all the features currently in GG2. The top level
  of the manual is https://www.pgdp.net/wiki/PPTools/Guiguts/Guiguts_2_Manual
- Pressing the F1 function key in any dialog brings up the manual page for
  that dialog
- Checker dialogs, e.g. Jeebies, now have a Copy Results button which copies
  all the messages from the dialog to the clipboard, so the user can paste
  them elsewhere to help with reporting issues or to analyze results
- Regex Cheat Sheet link added to Help menu
- Search dialog now has a First (or Last) button. This finds the first
  occurrence of the search term in the file (or last if Reverse searching).
  This is equivalent to Start at Beginning, followed by Search in GG1
- Each checker dialog, e.g. Jeebies and Spell check, now has its own settings
  for sorting the messages, either by line/column or by type/alphabetic
- PPtext now reports occurrences of multiple spaces/dashes once per line
  rather than every occurrence. The number of occurrences on the line
  is displayed in the error message 
- Detection of mid-paragraph illustrations/sidenotes has been improved
- Pressing "R&S" in the Search dialog after pressing Replace now does
  a Search
- Highlight colors have been adjusted for dark themes.

### Bug Fixes

- Ditto marks were not recognized if they appeared at the beginning or end
  of the line during curly quote conversion
- Blank lines at page breaks could be lost during rewrap
- Case changes required several Undo clicks to undo the changes made
- The text window could fail to scroll correctly when the mouse was clicked
  and dragged outside the window. Also other column-selection bugs.
- Multi-paragraph footnotes didn't "move to paragraph" correctly
- Illustration/Sidenote Fixup could move the wrong lines if the file had been
  edited since the tool was first run
- When selecting text to make an edit within an orange spotlighted piece of
  text, the selection was not visible
- Word Frequency and Search's ideas of what constitutes a word were
  inconsistent meaning that some "words" found by WF could not be found by
  searching
- Some ellipses were reported as "double punctuation" by PPtext
- Using Ctrl/Cmd+0 to fit the image to the image viewer window crashed if
  the image viewer was hidden at the time.


## Version 2.0.0-alpha.12

- There are no additional features - the primary reason for this release is
  to support macOS installation via `pip`

### Bug Fixes

- MacOS installation via `pip` failed due to out-of-date Levenshtein module
- Column selection failed in the lower of the split view windows
- Blank lines in indexes caused an error when rewrapped
- Dragging the cursor outside the window when scrolling failed on Macs
- The lower split view window colors didn't always match the theme
- Fractions with decimal points were converted wrongly



## Version 2.0.0-alpha.11

- Footnote Fixup dialog can now be used to fixup the majority of footnote
  situations, including setting up and moving footnotes to landing zones,
  or moving footnotes to the end of the paragraph. Mixed style footnotes
  are not yet supported.
- Text Markup dialog allows user to convert italic and other markup
- Clean Up Rewrap Markers removes rewrap markup from text file
- Stealth Scannos feature added
- Column numbers (horizontal ruler) can now be displayed
- Highlight Quotes & Brackets feature added
- Highlight Alignment column feature added
- Current line is now given a subtle background highlight
- Convert to Curly Quotes and Check Curly Quotes features added
- Image viewer background now adapts better to dark/light themes
- Insert cursor is now hidden when there is a selection
- Home/End keys (Cmd+Up/Down on Macs) go to start/end of checker dialogs,
  and Page Label Config dialog
- New shortcuts for Search/Replace: Cmd/Ctrl+Enter does Replace & Search;
  Shift+Cmd/Ctrl+Enter does Replace & Search in reverse direction
- Tooltips & labels improved in Preferences dialog

### Bug Fixes

- Double-clicking Re-run in checker dialogs caused an error
- Search/replace text fields were sometimes not tall enough to show character
- Show/hide line numbers now works properly in Split Window mode
- Some keystrokes, e.g. Ctrl+D, caused unwanted edits
- Word pairs followed by punctuation were not flagged in WF hyphen check
- Using cut/copy when macOS clipboard contained an image caused an error
- Illegal language codes were not handled well
- Fractions containing decimal points were wrongly converted
- Typing over a column selection gave unexpected results
- The page labels dialog could become desynchronized from the display


## Version 2.0.0-alpha.10

- Checker dialogs now use the same font as the text window
- Do not jump to position in main window when user uses the first-letter
  shortcut in Word Frequency
- Line.column displays in checker dialogs and Word Frequency are now padded
  and aligned 
- All features are now accessible via the menus (and hence by keyboard)
- Find Asterisks w/o Slashes feature added
- Words reported by spell checker can be added to global user dictionary
- Installation notes mention that either Python 3.11 or 3.12 can be used

### Bug Fixes

- Pasting didn't overwrite existing selection on Linux
- WF count and search did not handle word boundaries consistently
- Highlighting of spelling errors preceded by a single quote was wrong
- Fit-to-height sometimes failed in image viewer
- Double clicking Re-run button in checker dialogs caused an error


## Version 2.0.0-alpha.9

- Word Frequency Italic/Bold check is much faster, and when sorted
  alphabetically puts the marked up and non-marked up duplicates together
- Illustration Fixup tool added to facilitate moving illustrations to required
  location in file
- Sidenote Fixup tool added - similar to Illustration fixup
- Improvements to Image viewer including zoom, fit-to-width/height, dock and
  close buttons (shortcuts Cmd/Ctrl-plus, Cmd/Ctrl-minus and Cmd/Ctrl-zero);
  better zoomed image quality; ability to invert scan colors for dark themes;
  viewer size and position are remembered
- "Save a Copy As" button added to File menu
- Find Proofer Comments feature added
- Remove (unnecessary) Byte Order Mark from top of files

### Bug Fixes

- Word Frequency Hyphen check did not find suspects correctly
- Traceback occurred on Linux when Menu bar was selected - related to Split
  Text window code
- Keyboard shortcuts for Undo and Redo text edits did not work if the focus
  was in a checker tool dialog


## Version 2.0.0-alpha.8

- Split Text Window now available via the View menu
- Multi-replace now available in the Search/Replace dialog to show three
  independent replace fields with associated buttons
- Minor wording improvements to Preferences dialog
- Suspects Only checkbox in Word Frequency is now hidden when not relevant

### Known bugs discovered pre-testing alpha.8 (also in previous versions)

- Some false positives in Word Frequency hyphens check
- Some false positives in Ital/Bold/SC/etc check


## Version 2.0.0-alpha.7

- Unicode Search dialog added
- Unicode block list updated to include more recently defined blocks
- Warn user in Unicode dialogs if character is "recently added" to Unicode

### Bug Fixes

- Using `$` and `^` in regexes did not match end/start of line
- Some regex matches overlapped with the previous match
- Searching forward/backward did not always find the same matches - now does
  so, except in very rare case.
- `\C...\E` to execute bad Python code caused a traceback - now errors tidily


## Version 2.0.0-alpha.6

- Unicode & Commonly Used Characters dialog added
- Find All results improved for multiline matches
- Bad regexes in S/R dialog turn red as user types them

### Bug Fixes

- `Ctrl-left-click` in Basic Fixup caused an error
- S/R dialog kept resetting to a narrow width on Macs
- Searching for the next match in S/R didn't highlight correctly
- S/R regex count with backreferences didn't count correctly
- Replace All didn't work for all regexes
- Searching backwards for regex with backreference didn't work
- `^` didn't match beginning of all lines correctly
- Find Next/Previous key bindings (`F3`/`Cmd+g`) were executed twice
- Trying to use a bad regex caused an error - error now reported correctly
- Dock/Undock Image Window caused an error
- Compose sequence failed to insert some characters, e.g. non-breaking space
- Trailing hyphen appeared in title bar when there was no filename


## Version 2.0.0-alpha.5

- "Join Footnote to Previous" added to Footnote Fixup
- Status bar "current character" box now shows the selected character if
  exactly one character is selected, and nothing if more than one is
- Windows and Chromebook user installation notes added to README
- Navigation in Word Frequency dialog improved: Home & End keys go to
  start/end of list (Cmd Up/Down on Macs), Arrows and Page Up/Down
  scroll list, and typing a character jumps to the first word that 
  starts with that character, similar to GG1
- Levenshtein-based "Word Distance Check" added
- Search/Replace fields use same font & size as main window
- View-->Full Screen mode added (except on Macs)
- More powerful regex search/replace 
- `\C...\E` allows Python code to be run in regex replace
- Improved positioning of page breaks during multi-line regex replacements

### Bug Fixes

- Cursor wasn't placed consistently if user pressed left/right arrow while
  some text was selected. Now cursor goes to left/right of selection
- Footnote not processed correctly if not at start of line, e.g. after
  proofer's note
- Jeebies paranoia level radio buttons unexpectedly re-ran the tool
- Line number of current line wasn't always highlighted if a search
  changed line but didn't cause a scroll
- Compose sequence inserts didn't remove currently selected characters first
- Search dialog could get popped but without focus in the Search field,
  making it awkward to copy/paste the search string
- Lookahead and use of word boundary caused search strings not to be replaced


## Version 2.0.0-alpha.4

- Command line argument `--nohome` added which does not load the prefs file.
  This is primarily for testing purposes.
- Highlighted text in checker dialogs now uses the same colors as selected
  text in the main window.
- Text spotlighted in the main window by clicking on an error in a checker
  dialog is now highlighted in orange, rather than using selection colors
- Unmatched DP Markup now only checks for `i|b|u|g|f|sc`
- After fraction conversion, the cursor is placed after the last fraction
  converted, so it is clearer to the user what has happened
- The Spelling checker now supports spellcheck within selected text only
- The Spelling checker now has a threshold - if a word appears more times
  than the threshold, it is assumed to be good
- Unmatched Brackets and Curly Quotes now have a checkbutton to allow or
  disallow nesting
- A "working" label appears in checker dialogs when a tool is re-run, rather
  than showing "0 Entries"
- In the line numbers on the left, the number corresponding to the cursor's
  current location is highlighted 

### Bug Fixes

- Default scan directory `projectID0123456789abc_images` was not supported
- Errors occurred saving preferences if user's Documents directory was not
  in their home folder on Windows
- Page Separator Fixup started auto-fixing immediately if user changed
  radio buttons to Auto instead of waiting for user to click Refresh
- Additional blank lines were added during rewrapping
- After rewrapping a selection, the wrong range was selected


## Version 2.0.0-alpha.3

- Page Marker Flags now include the necessary information to generate the
  page labels, to improve transfer between GG2 and GG1 (v1.6.3 and above)
- Improved text rewrapping using Knuth-Plass algorithm (like Guiguts 1)
- Go to Img number no longer requires leading zeros
- A "Working" label and, on some platforms, a "busy" cursor now indicate
  when Guiguts is busy working on a long task.
- When user selects an entry in the Page Label Config dialog, the cursor
  jumps to the beginning of that page. If Auto Img is turned on, this will
  also show the scan image for that page
- If the full path to the text file is very long, its display in the title
  bar is truncated so that the name of the file is still visible

### Bug Fixes

- Cursor was not always visible after pasting text
- Word Frequency Ligature report included words that were not suspects
- Word Frequency Ital/Bold report is now sorted the same way as Guiguts 1
- Word Frequency Hyphens only reported the non-hyphenated form as suspect, 
  rather than both forms
- Unmatched quote check included some single quotes that were clearly
  apostrophes
- PPtxt was over-sensitive when reporting words appearing in hyphenated form
- Page Separator Fixup was leaving the page mark mid-word when a hyphenated
  word was joined
- Large files took far too long to load due to Page Marker Flags code


## Version 2.0.0-alpha.2

- Font family and size selection in Preferences (Edit menu)
- Highlight quotes in selection (Search menu)
- Additional Compose Sequences added (Cmd+I/Ctrl+I) such as curly quotes, 
  degrees, super/subscripts, fractions, Greek, etc. List of Sequences
  (Help Menu) allows clicking to insert character. 

### Bug Fixes

- Ignore Case in Word Frequency stopped options such as ALL CAPS from working
- Main window size and position didn't work well with maximized windows


## Version 2.0.0-alpha.1

First alpha release, containing the following features:
- Status bar with line/col, Img, Prev/See/Next Img, Lbl, selection, language,
  and current character display buttons
- Go to line, image, label (click in status bar)
- Restore previous selection (click in status bar)
- Change language (click in status bar)
- Line numbers (shift-click line/col in status bar)
- Normal and column selection supported for most operations
- Configure page labels (shift-click Lbl in status bar)
- Built-in basic image viewer (View menu)
- Auto Img (shift-click See Img in status bar)
- Recent documents (File menu)
- Change case features (Edit menu)
- Preferences (Edit menu, or Python menu on Macs) for theme, margins, etc
- Search & Replace (Search menu) with regex, match case, etc. Also, limit
  search/replace to current selection
- Count and Find All search features
- Bookmarks (Search menu, and via shortcuts)
- Basic Fixup (Tools menu)
- Word Frequency (Tools menu)
- Spell Check (Tools menu)
- PPtxt  (Tools menu)
- Jeebies (Tools menu)
- Fixup Page Separators (Tools menu)
- Fixup Footnotes (Tools menu) - begun but not complete
- Rewrap (Tools menu) - using "greedy" algorithm
- Unmatched Markup features  (Tools menu)
- Convert Fractions (Tools menu)
- Normalize Characters (Tools menu)
- Add/Remove Page Marker Flags (File-->Project menu) for transfer between
  editors
- Compose Sequences (Tools menu, and via Cmd+I/Ctrl+I shortcut) - only
  accented characters and Unicode ordinals. List of sequences (Help Menu)
- Message log (View menu)
- Command line arguments: 
    - `-h`, `--help`: show help on command line arguments
    - `-r1 (or 2...9)`, `--recent 1 (or 2...9)`: load most recent
      (or 2nd...9th most recent) file
    - `-d`: debug mode, mostly for developer use