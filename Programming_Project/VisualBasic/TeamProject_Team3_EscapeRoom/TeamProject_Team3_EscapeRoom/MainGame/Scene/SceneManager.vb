Public Class SceneManager
    Inherits Singleton(Of SceneManager)

    Private sceneDic As New Dictionary(Of String, Scene)
    Public Property pSceneDic As Dictionary(Of String, Scene)
        Get
            Return sceneDic
        End Get
        Set(value As Dictionary(Of String, Scene))
            sceneDic = value
        End Set
    End Property

    Private curSceneKey As String
    Public ReadOnly Property pCurSceneKey As String
        Get
            Return curSceneKey
        End Get
    End Property

    Public Sub Init()
        AddScene(New TitleScene("Title"))
        AddScene(New GameScene("Game"))
        AddScene(New EndingScene("Ending"))
    End Sub

    Public Sub AddScene(_scene As Scene)
        sceneDic.Add(_scene.pName, _scene)
    End Sub

    Public Function GetCurSceneKey() As String
        Return curSceneKey
    End Function

    Public Function GetCurScene() As Scene
        Dim tempScene As Scene = Nothing

        If sceneDic.ContainsKey(curSceneKey) Then
            If sceneDic.TryGetValue(curSceneKey, tempScene) Then
                Return tempScene
            End If
        End If

        Return Nothing
    End Function

    Public Function GetSceneByKey(keyName As String) As Scene
        Dim tempScene As Scene = Nothing

        If sceneDic.ContainsKey(keyName) Then
            If sceneDic.TryGetValue(keyName, tempScene) Then
                Return tempScene
            End If
        End If

        Return Nothing
    End Function

    Public Sub ChangeActiveScene(keyName As String)
        MainForm.Controls.Clear()

        Dim activeScene As Scene = Nothing

        If sceneDic.ContainsKey(keyName) Then
            If sceneDic.TryGetValue(keyName, activeScene) Then
                activeScene.SetScene()
                curSceneKey = activeScene.pName
            End If
        End If
    End Sub
End Class
