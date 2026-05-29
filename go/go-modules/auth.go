// Package jwtauth issues and verifies HS256 tokens using golang-jwt v4.
//
// On the v5 upgrade the import path changes (/v4 -> /v5) and the API breaks:
//   - jwt.StandardClaims is removed (use jwt.RegisteredClaims).
//   - RegisteredClaims time fields are *jwt.NumericDate, not int64.
//   - the Token.Valid bool field is gone; validity comes from the Parse error.
package jwtauth

import (
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v4"
)

// Issue signs a token for the given subject, valid for one hour.
func Issue(secret, subject string) (string, error) {
	// v4: StandardClaims with int64 unix timestamps.
	claims := jwt.StandardClaims{
		Subject:   subject,
		ExpiresAt: time.Now().Add(time.Hour).Unix(),
		IssuedAt:  time.Now().Unix(),
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString([]byte(secret))
}

// Verify parses the token and returns the subject if it is valid.
func Verify(secret, tokenString string) (string, error) {
	claims := &jwt.StandardClaims{}
	token, err := jwt.ParseWithClaims(tokenString, claims, func(t *jwt.Token) (interface{}, error) {
		if _, ok := t.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", t.Header["alg"])
		}
		return []byte(secret), nil
	})
	if err != nil {
		return "", err
	}
	// v4: Token.Valid is a bool field. Removed in v5.
	if !token.Valid {
		return "", fmt.Errorf("invalid token")
	}
	return claims.Subject, nil
}
