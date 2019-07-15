var tesseract = require('node-tesseract-ocr');
var fs = require("fs");
var path = require("path");

module.exports.OCRConvertor = class OCRConvertor{
    constructor(config){
        this.config = config;
    }

    async convertImageToText(filePath){
        const config = {
            lang: 'eng'
        }

        if (fs.existsSync(filePath)) {
            if(this.isImage(path.basename(filePath))){
                return await tesseract.recognize(filePath, config);
            }
            throw new Error(`File ${filePath} is not image type`);
        }
        throw new Error(`File ${filePath} does not exists`);
    }

    isImage(filePath){
        let fileext  = path.extname(filePath);
        return (this.config.imageTypes.find(type=> type === fileext)!= undefined);
    }
}