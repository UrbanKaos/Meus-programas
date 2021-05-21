VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} Pgm07vba02 
   Caption         =   "Ordenar"
   ClientHeight    =   6420
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   5490
   OleObjectBlob   =   "Pgm07vba02.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "Pgm07vba02"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
Dim A, B, C As Single
A = Val(TextBox1.Value)
B = Val(TextBox2.Value)
C = Val(TextBox3.Value)
If A = B And B = C And C = A Then
Label5.Caption = "Os valores são iguais"
Else
If A > B And A > C And B > C Then
Label5.Caption = "Os valores em ordem ascendente são:" + Str(C) + "," + Str(B) + "," + Str(A)
Else
If A > B And A > C And C > B Then
Label5.Caption = "Os valores em ordem ascendente são:" + Str(B) + "," + Str(C) + "," + Str(A)
Else
If B > A And B > C And A > C Then
Label5.Caption = "Os valores em ordem ascendente são:" + Str(C) + "," + Str(A) + "," + Str(B)
Else
If B > A And B > C And C > A Then
Label5.Caption = "Os valores em ordem ascendente são:" + Str(A) + "," + Str(C) + "," + Str(B)
Else
If C > A And C > B And A > B Then
Label5.Caption = "Os valores em ordem ascendente são:" + Str(B) + "," + Str(A) + "," + Str(C)
Else
If C > A And C > B And B > A Then
Label5.Caption = "Os valores em ordem ascendente são:" + Str(A) + "," + Str(B) + "," + Str(C)
End If
End If
End If
End If
End If
End If
End If
End Sub
