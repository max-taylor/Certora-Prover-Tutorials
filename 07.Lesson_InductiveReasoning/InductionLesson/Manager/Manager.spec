methods {
	getCurrentManager(uint256 fundId) returns (address) envfree
	getPendingManager(uint256 fundId) returns (address) envfree
	isActiveManager(address a) returns (bool) envfree
}


rule uniqueManager(uint256 fundId1, uint256 fundId2, method f ) {
	require fundId1 != fundId2;
  // Implication works here whereas an AND check doesn't
	require getCurrentManager(fundId1) != 0 => isActiveManager(getCurrentManager(fundId1));
	require getCurrentManager(fundId2) != 0 => isActiveManager(getCurrentManager(fundId2));
	require getCurrentManager(fundId1) != getCurrentManager(fundId2) ;
				
	env e;
	if (f.selector == claimManagement(uint256).selector)
	{
		uint256 id;
		require id == fundId1 || id == fundId2;
		claimManagement(e, id);  
	}
	else {
		calldataarg args;
		f(e,args);
	}
	assert getCurrentManager(fundId1) != getCurrentManager(fundId2), "managers not different";
	assert getCurrentManager(fundId1) != 0 => isActiveManager(getCurrentManager(fundId1)), "manager of fund1 is not active";
	assert getCurrentManager(fundId2) != 0 => isActiveManager(getCurrentManager(fundId2)), "manager of fund2 is not active";
}


 /* A start of uniqueManagerAsRule as an invariant, we will see in next lecture how to prove this */


// invariant uniqueManagerAsInvariant(uint256 fundId1, uint256 fundId2)
// 	fundId1 != fundId2 => (getCurrentManager(fundId1) != getCurrentManager(fundId2) && isActiveManager(getCurrentManager(fundId1)) && isActiveManager(getCurrentManager(fundId2)))
