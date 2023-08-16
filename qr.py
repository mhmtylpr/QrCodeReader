import qrcode as q
kodurl= input("lütfem bağlantı giriniz:  ")
file = q.make(kodurl)
type(file)
file.save("newwqr.png")