import streamlit as st
import numpy as np

def find_strictly_dominated_strategy(matrix, player):
    num_strategies = matrix.shape[0]
    for i in range(num_strategies):
        is_dominated = True
        for j in range(num_strategies):
            if i != j:
                if player == 1:
                    is_dominated = all(matrix[i, k] <= matrix[j, k] for k in range(num_strategies))
                else:
                    is_dominated = all(matrix[k, i] <= matrix[k, j] for k in range(num_strategies))
                if not is_dominated:
                    break
        if is_dominated:
            return i
    return None

def main():
    st.title("Elimination des stratégies dominées")

    st.sidebar.header("Entrez le nombre de stratégies pour chaque joueur")

    num_strategies_player1 = st.sidebar.number_input("Nombre de stratégies pour le joueur 1", min_value=2, step=1, value=2)
    num_strategies_player2 = st.sidebar.number_input("Nombre de stratégies pour le joueur 2", min_value=2, step=1, value=2)

    st.sidebar.header("Entrez la matrice de gains")

    player1_matrix = np.zeros((num_strategies_player1, num_strategies_player2))
    player2_matrix = np.zeros((num_strategies_player1, num_strategies_player2))

    for i in range(num_strategies_player1):
        for j in range(num_strategies_player2):
            player1_matrix[i][j] = st.sidebar.number_input(f"({i+1}, {j+1}) Payoff for Player 1", value=0)
    
    for i in range(num_strategies_player1):
        for j in range(num_strategies_player2):
            player2_matrix[i][j] = st.sidebar.number_input(f"({i+1}, {j+1}) Payoff for Player 2", value=0)

    st.sidebar.write("Payoff Matrix for Player 1:")
    st.sidebar.write(player1_matrix)

    st.sidebar.write("Payoff Matrix for Player 2:")
    st.sidebar.write(player2_matrix)

    # Find strictly dominated strategies for each player
    dominated_strategy_player1 = find_strictly_dominated_strategy(player1_matrix, player=1)
    dominated_strategy_player2 = find_strictly_dominated_strategy(player2_matrix, player=2)

    st.write("Solutions")
    if dominated_strategy_player1 is not None and dominated_strategy_player2 is not None:
        st.write(f"Solution pour le joueur 1: {dominated_strategy_player1} with payoff {player1_matrix[dominated_strategy_player1, dominated_strategy_player2]}")
        st.write(f"Solution pour le joueur 2: {dominated_strategy_player2} with payoff {player2_matrix[dominated_strategy_player1, dominated_strategy_player2]}")
    else:
        st.write("Pas de stratégies strictement dominées.")

if __name__ == '__main__':
    main()
