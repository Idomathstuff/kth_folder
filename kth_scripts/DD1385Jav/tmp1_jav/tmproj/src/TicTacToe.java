import java.util.Scanner;



public class TicTacToe 
{
    private static final int SIZE = 3; // Size of the game board
    private char[][] board; // Game board nxn
    private char currentPlayer; // Current player ('X' or 'O')

    public TicTacToe() {
        board = new char[SIZE][SIZE];
        currentPlayer = 'X';
        initializeBoard(); // puts characters in the board
    }

    // Initialize the game board
    private void initializeBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                board[i][j] = '-';
            }
        }
    }

    // Print the game board
    private void printBoard() { //prints the board char for char
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Play the game
    public void playGame() {
        Scanner scanner = new Scanner(System.in);
        int row, col;

        while (true) {
            System.out.println("Player " + currentPlayer + ", enter your move (row and column):");
            row = scanner.nextInt();
            col = scanner.nextInt();

            if (isValidMove(row, col)) {
                makeMove(row, col);

                // Check for a winner
                if (isWinner()) {
                    System.out.println("Player " + currentPlayer + " wins!");
                    break;
                }

                // Check for a draw
                if (isBoardFull()) {
                    System.out.println("It's a draw!");
                    break;
                }

                // Switch to the other player
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
            } else {
                System.out.println("Invalid move! Try again.");
            }

            printBoard();
        }
    }

    // Check if a move is valid
    private boolean isValidMove(int row, int col) {
        return (row >= 0 && row < SIZE && col >= 0 && col < SIZE && board[row][col] == '-');
    }

    // Make a move on the game board
    private void makeMove(int row, int col) {
        board[row][col] = currentPlayer;
    }

    // Check if there is a winner
    private boolean isWinner() {
        // Check rows
        for (int i = 0; i < SIZE; i++) {
            if (board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) {
                return true;
            }
        }

        // Check columns
        for (int j = 0; j < SIZE; j++) {
            if (board[0][j] == currentPlayer && board[1][j] == currentPlayer && board[2][j] == currentPlayer) {
                return true;
            }
        }

        // Check diagonals
        if (board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) {
            return true;
        }

        if (board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer) {
            return true;
        }

        return false;}



// // Check if the game board is full (draw)
    private boolean isBoardFull() {
            for (int i = 0; i < SIZE; i++) {
                for (int j=0; j < SIZE; j++){
                    if (board[i][j] == '-'){
                        return false;
                    }
                }
            }
            return true;
        }
    
    public static void main(String[] args){
        TicTacToe game = new TicTacToe();
        game.playGame();
    }
}