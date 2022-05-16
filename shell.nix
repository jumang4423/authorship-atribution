with import <nixpkgs> {};

( pkgs.python3.buildEnv.override  {
extraLibs = with pkgs.python35Packages; [ numpy toolz ];
}).envcl