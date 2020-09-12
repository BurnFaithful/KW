<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.bbs.Bbs, youngmin.web.bbs.BbsDAO" %>
<%@ page import="java.io.PrintWriter" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="../css/bootstrap.css">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="../js/bootstrap.js"></script>

    <title>영민이의 JSP 웹사이트</title>
</head>
<body>
<%
    PrintWriter script = response.getWriter();
    String userId = null;
    if (session.getAttribute("id") != null)
    {
        userId = (String)session.getAttribute("id");
    }
    int bbsId = 0;
    if (request.getParameter("bbsId") != null)
    {
        bbsId = Integer.parseInt(request.getParameter("bbsId"));
    }
    if (bbsId == 0)
    {
        script.println("<script>alert('유효하지 않은 글입니다.')");
        script.println("location.href='bbs.jsp'</script>");
    }
    Bbs bbs = new BbsDAO().getBbs(bbsId);
%>
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
        <%
            if (userId == null) {
        %>
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle"
                   data-toggle="dropdown" role="button" aria-haspopup="true"
                   aria-expanded="false">접속하기
                    <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li class="active"><a href="login.jsp">로그인</a></li>
                    <li><a href="join.jsp">회원가입</a></li>
                </ul>
            </li>
        </ul>
        <%
        } else {
        %>
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
        <%
            }
        %>
    </div>
</nav>
<div class="container">
    <div class="row">
        <form method="post" action="write_Action.jsp">
            <table class="table table-striped" style="text-align: center; border: 1px solid #dddddd">
                <thead>
                <tr>
                    <th colspan="3" style="background-color:#eeeeee; text-align: center;">게시판 글보기</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td style="width: 20%">글 제목</td>
                    <td colspan="2"><%= bbs.getBbsTitle() %></td>
                </tr>
                <tr>
                    <td>작성자</td>
                    <td colspan="2"><%= bbs.getUserID() %></td>
                </tr>
                <tr>
                    <td>작성일자</td>
                    <td colspan="2"><%= bbs.getBbsDate().substring(0, 11) +
                    bbs.getBbsDate().substring(11, 13) + "시 " +
                    bbs.getBbsDate().substring(14, 16) + "분" %></td>
                </tr>
                <tr>
                    <td>내용</td>
                    <td colspan="2" style="min-height: 200px; text-align: left;">
                        <%= bbs.getBbsContent().replaceAll(" ", "&nbsp;")
                                .replaceAll("<", "&lt;")
                                .replaceAll(">", "&gt;")
                                .replaceAll("\n", "</br>")
                                .replaceAll("\"", "&quot;")
                                .replaceAll("&", "&amp;")%></td>
                </tr>
                </tbody>
            </table>
            <a href="bbs.jsp" class="btn btn-primary">목록</a>
            <%
                if (userId != null && userId.equals(bbs.getUserID()))
                {
            %>
                <a href="update.jsp?bbsId=<%= bbsId %>" class="btn btn-primary">수정</a>
                <a onclick="return confirm('정말로 삭제하시겠습니까?')" href="delete_Action.jsp?bbsId=<%= bbsId %>" class="btn btn-primary">삭제</a>
            <%
                }
            %>
            <input type="submit" class="btn btn-primary pull-right" value="글쓰기">
        </form>
    </div>
</div>
</body>
</html>