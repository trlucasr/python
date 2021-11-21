function sendEmail() {
Email.send({
    Host : "smtp.hostinger.com.br",
    Username : "comunicacao@lagoinhaguarulhos.com",
    Password : "@IBL2020",
    To : 'tr.lucas@live.com',
    From : "comunicacao@lagoinhaguarulhos.com",
    Subject : "Teste",
    Body : "<html><h2>Header</h2><strong>Bold text</strong><br></br><em>Italic</em></html>"
}).then(
  message => alert(message)
);
}