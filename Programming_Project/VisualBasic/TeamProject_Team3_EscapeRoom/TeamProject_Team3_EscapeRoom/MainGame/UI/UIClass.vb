Public Class UIClass
    Inherits Singleton(Of UIClass)

    Private safePassword(6) As Label
    Public Property pSafePassword(ByVal index As Integer) As Label
        Get
            Return safePassword(index)
        End Get
        Set(value As Label)
            safePassword(index) = value
        End Set
    End Property

    Private questionBtn(5) As Button
    Public Property pQuestionBtn(ByVal index As Integer) As Button
        Get
            Return questionBtn(index)
        End Get
        Set(value As Button)
            questionBtn(index) = value
        End Set
    End Property

    Private questionMessage(5) As Question

    Public Sub SetUIPanel()
        MainForm.pUiPanel = New Panel() With
            {
                .Width = MainForm.ClientSize.Width,
                .Height = 200
            }
        MainForm.pUiPanel.Location = New Point(0, MainForm.ClientSize.Height - MainForm.pUiPanel.Height)
        MainForm.Controls.Add(MainForm.pUiPanel)

        For i = 0 To UBound(safePassword)
            safePassword(i) = New Label()
            safePassword(i).Width = 20
            safePassword(i).Height = 20
            safePassword(i).Text = DialLockForm.pPassword(i)
            safePassword(i).Font = New Font(Form.DefaultFont.FontFamily, 15, FontStyle.Bold)
            safePassword(i).Location = New Point(10 + safePassword(i).Width * i, 150)
            safePassword(i).Visible = False
            MainForm.pUiPanel.Controls.Add(safePassword(i))
        Next

        For i = 0 To UBound(questionMessage)
            questionMessage(i) = New Question()
            questionMessage(i).pId = i + 1
            Dim data As DataElement = Nothing
            If QuestionData.GetInstance().FindElementByKey("Id", questionMessage(i).pId, data) Then
                questionMessage(i).pQuestionText = data.DataIndexer("Text").value
                questionMessage(i).pQuestionAnswer = data.DataIndexer("Answer").value
            End If
        Next

        For i = 0 To UBound(questionBtn)
            questionBtn(i) = New Button()
            questionBtn(i).Name = i
            questionBtn(i).Width = 120
            questionBtn(i).Height = 30
            questionBtn(i).Text = "Question " & (i + 1)
            questionBtn(i).Font = New Font(Form.DefaultFont.FontFamily, 12, FontStyle.Bold)
            questionBtn(i).Location = New Point(875, 5 + questionBtn(i).Height * i + 10)
            questionBtn(i).Visible = False
            MainForm.pUiPanel.Controls.Add(questionBtn(i))
            AddHandler questionBtn(i).Click, AddressOf QuestionMessageBox
        Next
    End Sub

    Public Sub QuestionMessageBox(sender As Object, e As EventArgs)
        Dim tempBtn As Button = CType(sender, Button)
        Dim index As Integer = CInt(tempBtn.Name)
        Dim questionMsg As Question = questionMessage(index)

        If MsgBox(questionMsg.pQuestionText, MsgBoxStyle.OkCancel) = MsgBoxResult.Ok Then
            Dim answer As String = InputBox("답을 입력하세요.")

            If answer = questionMsg.pQuestionAnswer Then
                safePassword(index + 1).Visible = True
            End If
            questionBtn(index).Visible = True
        End If
    End Sub
End Class
