#include "SceneContainer.h"

void InitScene()
{

}

void ChangeScene(eSceneKind _sceneKind)
{
	curScene = sceneArr[_sceneKind];
}