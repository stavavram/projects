var multer = require('multer');

module.exports.Storage = class Storage{
    constructor(){
    }

    upload(){
       return multer({
            storage: multer.diskStorage({
                destination: "./uploads",
                filename: (req, file, cb) => {
                    cb(null, file.fieldname + '-' + Date.now())
                }
            })
        });
    }
}