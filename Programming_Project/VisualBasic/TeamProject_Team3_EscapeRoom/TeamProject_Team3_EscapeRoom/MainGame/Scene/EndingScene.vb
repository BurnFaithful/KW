Public Class EndingScene
    Inherits Scene

    Private bgPB As PictureBox

    Public Sub New(_name As String)
        MyBase.New(_name)
    End Sub

    Public Overrides Sub SetScene()

        bgPB = New PictureBox() With
            {
                .Width = MainForm.ClientSize.Width,
                .Height = MainForm.ClientSize.Height,
                .Image = GetResourceImage("endingBG"),
                .SizeMode = PictureBoxSizeMode.StretchImage
            }
        MainForm.Controls.Add(bgPB)

    End Sub

    Public Overrides Sub KeyInput(e As KeyEventArgs)
        Throw New NotImplementedException()
    End Sub
End Class
