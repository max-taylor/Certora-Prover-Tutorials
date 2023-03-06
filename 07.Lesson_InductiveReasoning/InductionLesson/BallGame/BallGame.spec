
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4() 
	ballAt() != 4 
  { preserved { require ballAt() == 1; } }

rule passSpec {
  require ballAt() == 1;
  method f; env e; calldataarg args;
	f(e, args);
  assert ballAt() != 4, "Ball at cannot be equal to 4";
}