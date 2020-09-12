Public Class PointerMaze
    Public Sub New()
        ' 디자이너에서 이 호출이 필요합니다.
        InitializeComponent()
        MoveTostart()
        ' InitializeComponent() 호출 뒤에 초기화 코드를 추가하세요.
    End Sub

    Private Sub MoveTostart()
        Dim startingpoint = Panel1.Location()
        startingpoint.Offset(10, 10)
        Cursor.Position = PointToScreen(startingpoint)
    End Sub

    Private Sub Wall_MouseEnter(sender As Object, e As EventArgs) Handles Panel1.MouseEnter, Label9.MouseEnter, Label8.MouseEnter, Label7.MouseEnter, Label6.MouseEnter, Label5.MouseEnter, Label4.MouseEnter, Label35.MouseEnter, Label34.MouseEnter, Label33.MouseEnter, Label32.MouseEnter, Label31.MouseEnter, Label30.MouseEnter, Label3.MouseEnter, Label29.MouseEnter, Label28.MouseEnter, Label27.MouseEnter, Label26.MouseEnter, Label25.MouseEnter, Label24.MouseEnter, Label23.MouseEnter, Label22.MouseEnter, Label21.MouseEnter, Label20.MouseEnter, Label2.MouseEnter, Label19.MouseEnter, Label18.MouseEnter, Label17.MouseEnter, Label16.MouseEnter, Label15.MouseEnter, Label14.MouseEnter, Label13.MouseEnter, Label12.MouseEnter, Label11.MouseEnter, Label10.MouseEnter, Label1.MouseEnter
        MoveTostart()
    End Sub
    Private Sub Finish_MouseEnter(sender As Object, e As EventArgs) Handles finish.MouseEnter
        'show a congratulatory massagebox, then close the form.
        If MsgBox("STUDY = 14136" & vbCrLf &
                  "PLAY = 3466" & vbCrLf &
                  "BATH = 3646" & vbCrLf &
                  "E = ?", MsgBoxStyle.OkCancel) = MsgBoxResult.Ok Then

            Dim answer As String = InputBox("답을 입력하세요.")

            If answer = 8 Then
                UIClass.GetInstance().pSafePassword(6).Visible = True
            End If
        End If
        UIClass.GetInstance().pQuestionBtn(5).Visible = True
        Me.Close()
    End Sub

    Private Sub PointerMaze_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class