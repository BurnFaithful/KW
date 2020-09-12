function checkLoginSession(attribute, nextPage)
{
    if (attribute != null)
    {
        alert("이미 로그인이 되어있습니다.");
        location.href = nextPage;
    }
}

function checkLoginResult(result, nextPage)
{
    if (result === 1)
    {
        alert("로그인 성공");
        location.href = nextPage;
    }
    else if (result === 0)
    {
        alert("비밀번호 틀림");
    }
    else if (result === -1)
    {
        alert("아이디 없음.");
    }
    else
    {
        alert("데이터베이스 오류.");
    }
}