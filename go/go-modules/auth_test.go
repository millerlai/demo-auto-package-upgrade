package jwtauth

import "testing"

const secret = "s3cr3t"

func TestIssueAndVerify(t *testing.T) {
	tok, err := Issue(secret, "ada")
	if err != nil {
		t.Fatalf("issue: %v", err)
	}
	sub, err := Verify(secret, tok)
	if err != nil {
		t.Fatalf("verify: %v", err)
	}
	if sub != "ada" {
		t.Fatalf("got subject %q, want %q", sub, "ada")
	}
}

func TestVerifyRejectsWrongSecret(t *testing.T) {
	tok, err := Issue(secret, "ada")
	if err != nil {
		t.Fatalf("issue: %v", err)
	}
	if _, err := Verify("wrong", tok); err == nil {
		t.Fatal("expected verification to fail with wrong secret")
	}
}
