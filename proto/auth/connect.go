package auth

import (
	"github.com/thedivinez/go-libs/utils"
)

func Connect(addr string) (AuthClient, error) {
	conn, err := utils.ConnectService(addr)
	if err != nil {
		return nil, err
	}
	return NewAuthClient(conn), nil
}
