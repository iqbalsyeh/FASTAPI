{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.imagemagick
    pkgs.tesseract
    pkgs.poppler_utils
  ];
}
