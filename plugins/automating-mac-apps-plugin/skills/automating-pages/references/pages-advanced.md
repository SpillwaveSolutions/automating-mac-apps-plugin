# Pages JXA advanced patterns

## AppleScript bridge for gaps
```javascript
function runAppleScript(code) {
  const app = Application.currentApplication();
  app.includeStandardAdditions = true;
  return app.runScript(code, { language: "AppleScript" });
}

const as = `
  tell application "Pages"
    tell front document
      make new table with properties {column count:4, row count:10}
    end tell
  end tell
`;
runAppleScript(as);
```

## Image insertion via clipboard (robust)
```javascript
function insertImage(imagePath) {
  const app = Application.currentApplication();
  app.includeStandardAdditions = true;
  app.doShellScript("osascript -e 'set the clipboard to (read (POSIX file \"" + imagePath + "\") as JPEG picture)'" );
  const pages = Application("Pages");
  pages.activate();
  const se = Application("System Events");
  se.keystroke("v", { using: "command down" });
  delay(0.5);
}
```

## Table population (pre-made template)
- Create a template document with a table.
- Open template, select the table, then write cell values.

