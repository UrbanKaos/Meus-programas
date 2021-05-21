VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm09 
   Caption         =   "UserForm1"
   ClientHeight    =   5940
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   5970
   OleObjectBlob   =   "Pgm09.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm09"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, S, R As Single
A = Val(TextBox1.Value)
S = (A * 25) / 100
R = A + S
Label3.Caption = "O aumento salarial foi de:" + Str(S) + " reais. E o novo sálario será de:" + Str(R) + " reais"
End Sub
