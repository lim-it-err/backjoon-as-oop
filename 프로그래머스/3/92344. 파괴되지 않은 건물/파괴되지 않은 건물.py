class PrefixSum2D:
    def __init__(self, board):
        self.prefix_board = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
        self.board = board
    def act(self, skill):
        # (0, 0)부터 (3, 4)까지 공격하여 4만큼 내구도를 낮추면
        # prefix_sum[0][0] -=4
        # prefix_sum[0][5] = 4
        # prefix_sum[5][0] = 4
        # prefix_sum[5][5] = -4
        t, r1, c1, r2, c2, degree = skill
        if t == 1:
            degree = -degree
        self.prefix_board[r1][c1] +=degree
        self.prefix_board[r1][c2+1] -=degree
        self.prefix_board[r2+1][c1] -=degree
        self.prefix_board[r2+1][c2+1] +=degree
    def apply(self):
        answer = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if j == 0:
                    continue
                self.prefix_board[i][j] += self.prefix_board[i][j-1]
        
        for j in range(len(self.board[0])):
            for i in range(len(self.board)):
                if i == 0:
                    continue
                self.prefix_board[i][j] += self.prefix_board[i-1][j]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] += self.prefix_board[i][j]
                if self.board[i][j] > 0:
                    answer+=1
        return answer
def solution(board, skills):
    answer = 0
    prefix_agent = PrefixSum2D(board)
    for skill in skills:
        prefix_agent.act(skill)

    return prefix_agent.apply()