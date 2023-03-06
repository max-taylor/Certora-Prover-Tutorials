certoraRun ReserveListFixed.sol:ReserveList --verify ReserveList:ReserveList.spec \
--solc solc \
--optimistic_loop \
--send_only \
--loop_iter 3 \
--msg "correlated lists broken"

# --optimistic_loop and --loop_iter 3 are flags that handle loops.
# They are needed here, but don't mind them, you will learn about loop handling in a future lesson.