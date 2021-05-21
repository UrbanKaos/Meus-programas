VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm08 
   Caption         =   "UserForm1"
   ClientHeight    =   5520
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   5445
   OleObjectBlob   =   "Pgm08.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm08"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, R As Single
A = Val(TextBox1.Value)
R = (A * 5) / 100
Label3.Caption = "O imposto de renda a ser pago é:" + Str(R) + " reais"
End Sub
