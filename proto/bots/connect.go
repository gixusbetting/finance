package bots

import (
	"github.com/thedivinez/go-libs/storage"
	"github.com/thedivinez/go-libs/utils"
)

type Client struct {
	Client BotsClient
	Redis  *storage.RedisCache
}

func NewClient(host string) *Client {
	return &Client{Redis: storage.NewRedisCache(host)}
}

func (client *Client) Connect(addr string) error {
	conn, err := utils.ConnectService(addr)
	if err != nil {
		return err
	}
	client.Client = NewBotsClient(conn)
	return nil
}
