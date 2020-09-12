<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.bbs.Bbs, youngmin.web.bbs.BbsDAO" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="../css/bootstrap.css">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="../js/bootstrap.js"></script>
    <script>
        function validate()
        {
            var title = document.getElementById("bbsTitle");
            var content = document.getElementById("bbsContent");

            if (!title.value || !content.value)
            {
                alert("글 제목과 글 내용은 반드시 입력해야 합니다.");
                history.back();
                return false;
            }
            return true;
        }

        function checkSession(sessionValue)
        {
            if (sessionValue == null)
            {
                alert("로그인이 필요합니다.");
                location.href = "login.jsp";
            }
        }

        function checkAuthority(id)
        {
            if (id == null)
            {
                alert("권한이 없습니다!");
                location.href = "bbs.jsp";
            }
        }
    </script>

    <title>영민이의 JSP 웹사이트</title>
</head>
<body>
<%
    String userId = null;
    if (session.getAttribute("id") != null)
    {
        userId = (String)session.getAttribute("id");
    }
%>
    <script>checkSession("<%= userId %>");</script>
<%
    int bbsId = 0;
    if (request.getParameter("bbsId") != null)
        bbsId = Integer.parseInt(request.getParameter("bbsId"));
%>
    <script>checkAuthority(<%= bbsId %>);</script>
<%
    Bbs bbs = new BbsDAO().getBbs(bbsId);
%>
    <script>checkAuthority(<%= !userId.equals(bbs.getUserID()) %>);</script>
<nav class="navbar navbar-default">
    <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed"
                data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
                aria-expanded="false">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="main.jsp">영민이의 JSP 웹사이트</a>
    </div>
    <div class="collapse navbar-collapse" id="#bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
            <li><a href="main.jsp">메인</a></li>
            <li class="active"><a href="bbs.jsp">게시판</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle"
                   data-toggle="dropdown" role="button" aria-haspopup="true"
                   aria-expanded="false">회원관리
                    <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="logout_Action.jsp">로그아웃</a></li>
                </ul>
            </li>
        </ul>
    </div>
</nav>
<div class="container">
    <div class="row">
        <form method="post" onsubmit="return validate()" action="update_Action.jsp">
            <table class="table table-striped" style="text-align: center; border: 1px solid #dddddd">
                <thead>
                <tr>
                    <th colspan="2" style="background-color:#eeeeee; text-align: center;">게시판 글 수정 양식</th>
                    <input type="hidden" id="bbsId" name="bbsId" value="<%= bbs.getBbsID() %>"/>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td><input type="text" class="form-control" placeholder="글 제목" id="bbsTitle" name="bbsTitle" maxlength="50" value="<%= bbs.getBbsTitle() %>"></td>
                </tr>
                <tr>
                    <td><textarea class="form-control" placeholder="글 내용" id="bbsContent" name="bbsContent" maxlength="2048" style="height: 350px;"><%= bbs.getBbsContent() %></textarea></td>
                </tr>
                </tbody>
            </table>
            <input type="submit" class="btn btn-primary pull-right" value="글 수정">
        </form>
    </div>
</div>
</body>
</html>