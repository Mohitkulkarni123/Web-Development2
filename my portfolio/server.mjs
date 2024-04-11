const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
    host: "smtp.qwe.io",
    port: 465,
    secure: true,
    auth: {
        user: "mohitkulkarni2003@gmail.com",
        pass: "Reva@2007",
    },
});

const mailOptions = {
    from: "mohitkulkarni2003@gmail.com",
    to: "pvkulkarni72@gmail.com",
    subject: "This is a subject",
    text: "this is the body",
};

transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
        return console.log(error);
    }
    console.log("Message sent: %s", info.messageId);
});