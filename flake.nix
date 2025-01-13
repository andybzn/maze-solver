{
  description = "A Python Maze Solver";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
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

        formatScript = pkgs.writeScriptBin "format" ''
          #!${pkgs.bash}/bin/bash

          show_usage() {
            echo "Format Python code using Black"
            echo "Usage:"
            echo "  * format check - Check file formatting"
            echo "  * format fix - Format all files in project"
          }

          case "$1" in
            "check")
              ${pkgs.black}/bin/black --check .
              ;;
            "fix")
              ${pkgs.black}/bin/black .
              ;;
            *)
              show_usage
              ;;
          esac
        '';

      in
      {
        packages.default = buildScript;
        devShells.default = pkgs.mkShell {
          packages = [ pkgs.zsh ];
          buildInputs = [
            pkgs.python312Full
            pkgs.black
            pkgs.basedpyright
            buildScript
            testScript
            formatScript
          ];

          shellHook = ''
            export SHELL=${pkgs.zsh}/bin/zsh

            echo "Development environment loaded!"
            echo "Available commands:"
            echo "  * build - Run the maze solver"
            echo "  * tests - Execute unit tests"
            echo "  * format check - Check file formatting"
            echo "  * format fix - Format files in project"

            if [[ $SHELL != ${pkgs.zsh}/bin/zsh ]]; then
              exec ${pkgs.zsh}/bin/zsh
            fi
          '';
        };
      }
    );
}
