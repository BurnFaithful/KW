Public Class TitleScene
    Inherits Scene

    Private bgPB As PictureBox
    Private startBtn As PictureBox
    Private exitBtn As PictureBox

    Public Const BUTTON_IMAGE_GAP As Integer = 17

    Public Sub New(_name As String)
        MyBase.New(_name)
    End Sub

    Public Overrides Sub SetScene()
        bgPB = New PictureBox() With
            {
                .Width = MainForm.ClientSize.Width,
                .Height = MainForm.ClientSize.Height,
                .Image = GetResourceImage("titleBG"),
                .SizeMode = PictureBoxSizeMode.StretchImage
            }
        MainForm.Controls.Add(bgPB)

        ' Button
        startBtn = New PictureBox() With
            {
                .Image = GetResourceImage("startBtn"),
                .SizeMode = PictureBoxSizeMode.AutoSize
            }
        startBtn.Location = New Point((MainForm.ClientSize.Width - startBtn.Width) / 2,
                                      (MainForm.ClientSize.Height - startBtn.Height) / 2)
        bgPB.Controls.Add(startBtn)
        AddHandler startBtn.Click, AddressOf Event_StartBtnClick
        AddHandler startBtn.MouseEnter, AddressOf Event_StartBtn_MouseOver
        AddHandler startBtn.MouseLeave, AddressOf Event_StartBtn_MouseLeave

        exitBtn = New PictureBox() With
            {
                .Image = GetResourceImage("exitBtn"),
                .SizeMode = PictureBoxSizeMode.AutoSize
            }
        exitBtn.Location = New Point((MainForm.ClientSize.Width - exitBtn.Width) / 2,
                                     startBtn.Location.Y + startBtn.Height + BUTTON_IMAGE_GAP)
        bgPB.Controls.Add(exitBtn)
        AddHandler exitBtn.Click, AddressOf Event_ExitBtnClick
        AddHandler exitBtn.MouseEnter, AddressOf Event_ExitBtn_MouseOver
        AddHandler exitBtn.MouseLeave, AddressOf Event_ExitBtn_MouseLeave
        ' Button
    End Sub

    Public Overrides Sub KeyInput(e As KeyEventArgs)
        Throw New NotImplementedException()
    End Sub

    Public Sub Event_StartBtnClick()
        SceneManager.GetInstance().ChangeActiveScene("Game")
    End Sub

    Public Sub Event_ExitBtnClick()
        MainForm.Close()
    End Sub

    Public Sub Event_StartBtn_MouseOver()
        startBtn.Image = GetResourceImage("startBtn_over")
    End Sub

    Public Sub Event_StartBtn_MouseLeave()
        startBtn.Image = GetResourceImage("startBtn")
    End Sub

    Public Sub Event_ExitBtn_MouseOver()
        exitBtn.Image = GetResourceImage("exitBtn_over")
    End Sub

    Public Sub Event_ExitBtn_MouseLeave()
        exitBtn.Image = GetResourceImage("exitBtn")
    End Sub
End Class
