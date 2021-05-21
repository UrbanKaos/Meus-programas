VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm01 
   Caption         =   "UserForm1"
   ClientHeight    =   4410
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4920
   OleObjectBlob   =   "Pgm01.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm01"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, B, C As Integer
A = Val(TextBox1.Value)
B = Val(TextBox2.Value)
C = A * B
Label4.Caption = "O resultado da multiplicação é:" + Str(C)
End Sub
