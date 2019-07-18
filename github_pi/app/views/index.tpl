<!DOCTYPE html>
<html>
  <body>
    % for package in packages:
      <a href="/{{package}}/">{{package}}</a>
    % end
  </body>
</html>