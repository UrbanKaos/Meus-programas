VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm04 
   Caption         =   "UserForm1"
   ClientHeight    =   5925
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   5925
   OleObjectBlob   =   "Pgm04.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm04"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, B, R As Single
A = Val(TextBox1.Value)
B = Val(TextBox2.Value)
R = A / B
Label4.Caption = "O funcionário recebe" + Str(R) + " salários minimos"
End Sub
