Public MustInherit Class Scene
    Implements IScene

    Public Enum eSceneKind
        TITLE
        GAME
        ENDING
    End Enum

    Protected sceneKind As eSceneKind
    Public Property pSceneKind As eSceneKind
        Get
            Return sceneKind
        End Get
        Set(value As eSceneKind)
            sceneKind = value
        End Set
    End Property
    Protected name As String
    Public Property pName As String
        Get
            Return name
        End Get
        Set(value As String)
            name = value
        End Set
    End Property

    Protected Sub New(_name As String)
        name = _name
    End Sub

    Public MustOverride Sub SetScene() Implements IScene.SetScene
    Public MustOverride Sub KeyInput(e As KeyEventArgs) Implements IScene.KeyInput

    Public Overridable Sub Event_ScrollTimer_Tick() Implements IScene.Event_ScrollTimer_Tick
    End Sub

    Public Overridable Sub Event_DialogTimer_Tick() Implements IScene.Event_DialogTimer_Tick
    End Sub
End Class
