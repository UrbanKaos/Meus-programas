VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm10 
   Caption         =   "UserForm1"
   ClientHeight    =   8415.001
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   6810
   OleObjectBlob   =   "Pgm10.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm10"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim salmin, qtdekw, kwgasto, multikw, desckw, kwfinal As Single
salmin = Val(TextBox1.Value)
kwgasto = Val(TextBox2.Value)
qtdekw = salmin / 5
multikw = qtdekw * kwgasto
desckw = (multikw * 15) / 100
kwfinal = (multikw - desckw)
Label4.Caption = "O valor, em reais, de cada quilowatt é de:" + Str(qtdekw) + " reais"
Label5.Caption = "O valor, em reais, a ser pago por essa residência é de:" + Str(multikw) + " reais"
Label6.Caption = "O valor do desconto foi de:" + Str(desckw) + " reais. E o novo valor a ser pago é de:" + Str(kwfinal) + " reais"
End Sub
