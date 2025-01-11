{
  description = "A Python Maze Solver";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = nixpkgs.legacyPackages.${system};

      buildScript = pkgs.writeScriptBin "build" ''
        #!${pkgs.bash}/bin/bash
        PYTHONPATH=$PYTHONPATH:. ${pkgs.python312Full}/bin/python3 -m src.main
      '';

      testScript = pkgs.writeScriptBin "tests" ''
	#!${pkgs.bash}/bin/bash
	PYTHONPATH=$PYTHONPATH. ${pkgs.python312Full}/bin/python3 -m unittest discover -s tests
      '';
    in 
  {
    # pakages.default = mainPackage;
    devShells.default = pkgs.mkShell {
      packages = [ pkgs.zsh ];
      buildInputs = [
        pkgs.python312Full
        pkgs.black
        pkgs.basedpyright
        buildScript
	testScript
      ];

      shellHook = ''
        export SHELL=${pkgs.zsh}/bin/zsh
      
        if [[ $SHELL != ${pkgs.zsh}/bin/zsh ]]; then
          exec ${pkgs.zsh}/bin/zsh
        fi
      '';
    };
  });
}
