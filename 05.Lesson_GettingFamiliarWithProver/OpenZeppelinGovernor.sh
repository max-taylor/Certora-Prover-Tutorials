certoraRun certora/harnesses/ERC20VotesHarness.sol certora/harnesses/GovernorHarness.sol \
    --verify GovernorHarness:certora/specs/GovernorBase.spec \
    --solc solc \
    --optimistic_loop \
    --settings -copyLoopUnroll=4 \
    --rule voteStartBeforeVoteEnd \
    --msg "$1"
