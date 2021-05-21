VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm06 
   Caption         =   "UserForm1"
   ClientHeight    =   5115
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   6105
   OleObjectBlob   =   "Pgm06.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm06"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, R As Single
A = Val(TextBox1.Value)
R = A * A
Label3.Caption = "A área do quadrado, sendo os lados todos iguais, será:" + Str(R)
End Sub
