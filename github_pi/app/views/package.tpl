<!DOCTYPE html>
<html>
  <head>
    <title>Links for {{package_name}}</title>
  </head>
  <body>
  <h1>Links for tqdm</h1>
    % for asset_name, asset_url in assets.items():
      <a href="{{asset_url}}">{{asset_name}}</a><br/>
    % end
  </body>
</html>