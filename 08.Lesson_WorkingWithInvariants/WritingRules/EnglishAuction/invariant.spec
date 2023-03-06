
/*
   This is a specification file for EnglishAuction's formal verification
   using the Certora prover.
 */
 



/*
    Declaration of methods that are used in the rules. envfree indicate that
    the method is not dependent on the environment (msg.value, msg.sender).
    Methods that are not declared here are assumed to be dependent on env.
*/


methods {
    // auction getters 
    seller() returns (address)                                              envfree
    nftId() returns (uint)                                                  envfree
    nft() returns(address)                                                  envfree
    endAt() returns (uint256)                                               envfree
    started() returns (bool)                                                envfree
    ended() returns (bool)                                                  envfree
    highestBidder() returns (address)                                       envfree
    highestBid() returns (uint256)                                          envfree
    bids(address) returns (uint256)                                         envfree
    operators(address, address) returns (bool)                              envfree
}

invariant zeroHighestBid(address other) 
  (highestBid() == 0 || highestBidder() == 0) => bids(other) == 0
  {
    preserved bidFor(address bidder, uint256 amount) {
      require bidder != 0;
    }
    preserved bid(uint256 amount) with (env e) {
      require e.msg.sender != 0;
    }
  }

// check highestBidder correlation with highestBid from bids mapping
invariant highestBidVSBids(address user) 
    (highestBidder() == user => bids(user) == highestBid()) || 
    (highestBidder() == 0)


// Nobody can have more bids than highestBid
invariant integrityOfHighestBidWeak(address any) 
    bids(any) <= highestBid()


// others have less than highestBid
invariant integrityOfHighestBid(address other) 
    other != highestBidder() =>  bids(other) < highestBid() 

invariant integrityOfHighestBidOther(address other)
  (highestBid() > 0 && other != highestBidder()) => bids(other) < highestBid()
  {
    preserved {
        requireInvariant highestBidVSBids(other);
        requireInvariant zeroHighestBid(other);
    }
  }