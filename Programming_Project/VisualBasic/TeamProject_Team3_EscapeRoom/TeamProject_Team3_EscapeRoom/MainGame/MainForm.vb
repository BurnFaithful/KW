Public Class MainForm

    Public rm As Resources.ResourceManager = New Resources.ResourceManager("TeamProject_Team3_EscapeRoom.Resources", Reflection.Assembly.GetExecutingAssembly)

    Private uiPanel As Panel
    Public Property pUiPanel As Panel
        Get
            Return uiPanel
        End Get
        Set(value As Panel)
            uiPanel = value
        End Set
    End Property

    Private curEventId As Integer ' Main Event Current Id
    Public Property pCurEventId As Integer
        Get
            Return curEventId
        End Get
        Set(value As Integer)
            curEventId = value

            If curEventId = 0 Then
                SceneManager.GetInstance().ChangeActiveScene("Ending")
            End If
        End Set
    End Property

    Private useItemId As Integer
    Public Property pUseItemId As Integer
        Get
            Return useItemId
        End Get
        Set(value As Integer)
            useItemId = value
        End Set
    End Property

    Private Sub MainForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        SetForm()
        ResourceLoad()
        Init()
    End Sub

    Private Sub SetForm()
        Me.Text = WINDOWS_NAME
        Me.Width = WINDOWS_WIDTH
        Me.Height = WINDOWS_HEIGHT
    End Sub

    Private Sub ResourceLoad()
        ' Parsing Data Load
        PropData.GetInstance().LoadData()
        ItemData.GetInstance().LoadData()
        DialogData.GetInstance().LoadData()
        QuestionData.GetInstance().LoadData()
        ' Parsing Data Load
    End Sub

    Private Sub Init()
        pCurEventId = 1
        pUseItemId = 0

        SceneManager.GetInstance().Init() ' 씬 매니저 초기화
        SceneManager.GetInstance().ChangeActiveScene(GAME_STARTSCENE)
    End Sub

    Private Sub MainForm_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown
        SceneManager.GetInstance().GetCurScene().KeyInput(e)
    End Sub

    Private Sub ScrollTimer_Tick(sender As Object, e As EventArgs) Handles ScrollTimer.Tick
        SceneManager.GetInstance().GetCurScene().Event_ScrollTimer_Tick()
    End Sub

    Private Sub DialogTimer_Tick(sender As Object, e As EventArgs) Handles DialogTimer.Tick
        SceneManager.GetInstance().GetCurScene().Event_DialogTimer_Tick()
    End Sub
End Class
