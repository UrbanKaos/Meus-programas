VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm03 
   Caption         =   "UserForm1"
   ClientHeight    =   5580
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   5235
   OleObjectBlob   =   "Pgm03.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm03"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, B, res, rend As Single
A = Val(TextBox1.Value)
B = Val(TextBox2.Value)
rend = (A * B) / 100
res = rend + A
Label4.Caption = "O rendimento foi de:" + Str(Round(rend, 2)) + " reais. E o rendimento total foi de:" + Str(Round(res, 2)) + " reais"
End Sub
