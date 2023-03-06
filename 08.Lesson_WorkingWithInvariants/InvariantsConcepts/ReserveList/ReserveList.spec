methods {
  getTokenAtIndex(uint256 index) returns (address) envfree
  getIdOfToken(address token) returns (uint256) envfree
  getReserveCount() returns (uint256) envfree
  addReserve(address token, address stableToken, address varToken, uint256 fee) envfree
  removeReserve(address token) envfree
}

invariant mappingCorrelation(uint256 index, address token)
  (( index != 0 && token != 0 ) => (getTokenAtIndex(index) == token <=> getIdOfToken(token) == index)) 
            &&
	(( index == 0 && token !=0 ) => (getTokenAtIndex(index) == token => getIdOfToken(token) == index))
        {
            preserved
            {
                requireInvariant indexLessThanCount(token);
            }
            
            preserved removeReserve(address t) {
			    require t == token;
		    }
      }