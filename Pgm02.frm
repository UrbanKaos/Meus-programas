VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm02 
   Caption         =   "UserForm1"
   ClientHeight    =   6735
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   5925
   OleObjectBlob   =   "Pgm02.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm02"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, B, C, D, R As Single
A = Val(TextBox1.Value)
B = Val(TextBox2.Value)
C = Val(TextBox3.Value)
D = Val(TextBox4.Value)
R = (A + B + C + D) / 4
Label6.Caption = "A média aritmética do aluno é:" + Str(R)
End Sub
