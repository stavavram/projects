var container = require('../containerConfig');
var multer = require('multer');
//var uploader = container.get('storage');
//var upload = uploader.upload()
var upload = multer({
    storage: multer.diskStorage({
        destination: "./uploads",
        filename: (req, file, cb) => {
            cb(null, file.fieldname + '-' + Date.now())
        }
    })
}).single("upfile");
module.exports.uploadFile = (upload, function (req, res, next) {

    /*upload(req, res, function (err) {
        if (err){
            res.end(err.message);
        }else{
            // If file is not selected
            if (req.file == undefined) {
                res.end('No file selected!');

            }
            else{
                res.end('File uploaded successfully!');
            }
        }
    });*/
});

/*(req, res, function (err) {

    });*/