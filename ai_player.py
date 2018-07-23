'''Onur Çopur
Dilara Işıklı
Chunhui Wu
'''
import abc
import logging
import random
import utils

from player import Player
from board import Board
from game import Game


class AIPlayer(Player):
    '''
    If I win then I will get 999
           If opposite win I will get -999
           No one win,then return 0
    '''
    def evaluate(self,board,pos):
        '''score=0
        for i in  range(0,board.num_cols):
            test=board.getCol(i)
            color, size = utils.longest(test)
            if size==3:
                if self.color==color:
                    score=score+10
                else:
                    score=score-10
            elif size==2:
                if self.color==color:
                    score=score+5
                else:
                    score=score-5
        for i in  range(0,board.num_rows):
            test=board.getRow(i)
            color, size = utils.longest(test)
            if size>=2:
                if self.color==color:
                    score=score+10
                else:
                    score=score-10
            elif size==2:
                if self.color==color:
                    score=score+5
                else:
                    score=score-5
                
        return score
        '''
        row0=[]
        mat0=[]
        rowcn=board.num_rows
        colcn=board.num_cols
        score=-138
        mat0=[[3, 4, 5, 7, 5, 4, 3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4],[3, 4, 5, 7, 5, 4, 3]]
        mat1=[]
        for i in range(board.num_cols):
            mat1.append(board.getCol(i))
        for i in range(0,colcn):
            for j in range(0,rowcn):
                if mat1[i][j]==self.color:
                    score=score+mat0[j][i]
        return score
    def playerGetWinner(self, board,pos):
        test=board.getCol(pos[0])
        color, size = utils.longest(test)
#        print(pos[1])  // debug only
        
        '''
        this is for deciding the winners
        '''
        
        if size < 4:
            test=board.getRow(pos[1])
            color, size = utils.longest(test)
            if size < 4:
                test=board.getDiagonal(True, pos[0] - pos[1])
                color, size = utils.longest(test)
                if size < 4:
                    test=board.getDiagonal(False, pos[0] + pos[1])
                    color, size = utils.longest(test)
                    if size < 4:
                        return self.evaluate(board,pos)
        if self.color==color:
            return 999
        else :
            return -999
               
        
        
#    useless function (maybe useful in the future OvO)    
#    def isFinish(self,board,col,):
#        row=board.getHeight(col)
#        pos=(col,row)
#        board.play(self,col)
#        return self.playerGetWinner(board,pos)
        
       
    """main function to return a colomn"""
    def getColumn(self, board):
#        print(board.getRow())  debug only
        board1=board
        columns = board1.getPossibleColumns()
        if columns:
            mat=self.observe(board1,1)
#            print(super(board))  debug only
            test=[]
            chooselist=[]  #this is for choosing from multiple values
            test=self.minimax(board1,3,True)
            print(test)   #currently using for debug
            
            max=-999   #'''the beginning of our choice'''
            for i,score in test:
                if score>max:
                    max=score
                    chooselist=[i]
                elif score==max:
                    chooselist.append(i)
                    
            return random.choice(chooselist)
        
    '''use this function to get the matrix of the board'''
    def observe(self,board,winner):
        mat1=[]
        for i in range(board.num_cols):
            mat1.append(board.getCol(i))
        return mat1
    
    '''main decision function applying minimax,but no alpha-beta yet'''
    
    def minimax(self,board,depth,player):
        '''depth：how deep the function will go,currently it's 3
            player:1==>AI,0==>opposite'''
        board1=board
        mat1=self.observe(board1,0)
        if depth==0:#when depth=0 return the values of all the nodes, 0 for undecided situations
            test=[]
            for j in board1.getPossibleColumns():
                
                row2=board1.getHeight(j)
                pos=(j,row2)
                if player==True: 
                    mat1[j][row2]=self.color
                else:
                    mat1[j][row2]=-self.color
                test.append((j,self.playerGetWinner(board1,pos)))
                mat1[j][row2]=0
            return test
        else:
            #initialize
            test_o=[]
            testing=0
            
            for i in board1.getPossibleColumns():#this is the quiry circle
                row=board1.getHeight(i)
                test_i=[]
                row=board1.getHeight(i)
                if row>board1.num_rows:#if the colomn is full ,skip it
                    continue
                pos=(i,row)
                if player==True: 
                    mat1[i][row]=self.color
                else:
                    mat1[i][row]=-self.color
                testing=self.playerGetWinner(board,pos)
                if testing==999 or testing==-999:#if this is a leaf node ,skip searching
                    test_o.append((i,testing))
                    mat1[i][row]=0
                else:#if this node has children,we go deeper
                    min=999
                    max=-999
                    test_i=self.minimax(board1,depth-1,not player)
                    
                    if player==0:#last player is opposite,it's our turn,maxmize
                        for j,score in test_i:
                            if score>max:
                                max=score
                                im=j
                        test_o.append((i,max))
                    
                    if player==1:#last player is ai,minimize
                        for j,score in test_i:
                            if score<min:
                                min=score
                                im=j
                        test_o.append((i,min))
                    mat1[i][row]=0
            return  test_o
                