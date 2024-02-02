{ lib, python310Packages }:
with python310Packages;
buildPythonPackage {
  name = "github-reporter";
  version = "1.0.0";

  format = "pyproject";

  buildInputs = [ setuptools pip ];

  src = ./.;
}
