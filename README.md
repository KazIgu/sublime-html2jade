# HTML to JADE plugin for Sublime Text 3

Converts files, selection and clipboard content from HTML to JADE using the [htm2jade](https://github.com/donpark/html2jade).

## Installation

### Git installation

Clone the repository in your Sublime Text "Packages" directory:

    git clone git@github.com:KazIgu/sublime-html2jade.git "HTML2Jade"

The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 3/Packages/

## Setting

You have to set binDir.

`Preferences > Package Settings > html2jade > Settings – User`

Example

    {
      "binDir": "/Users/kazigu/.nodebrew/current/bin"
    }

If you don't know "binDir", you can use `which html2jade`


## Usage

* **Convert selection** `super+j` - replaces selection of HTML with Jade content.
* **Convert clipboard content** `super+ctrl+j` - inserts Jade of converted clipboard HTML content.


### In Command Palette:

* **HTML2Jade: Convert file**
* **HTML2Jade: Convert selection**
* **HTML2Jade: Convert clipboard content**