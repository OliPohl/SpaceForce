using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    ####################################################
    #            PlayerControllerScript.cs             #
    #--------------------------------------------------#
    # This script makes the player move and shoot.     #
    #                                                  #
    # Speed/Reload time is given in: GameSettings.cs   #
    ####################################################
*/  
public class PlayerControllerScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] public GameObject Projectile;

    private Rigidbody2D PlayerRigidbody;

    private float nextFire = 0.0f;
    

    void Start()    // Gets the Players rigidbody
    {   
        PlayerRigidbody = GetComponent<Rigidbody2D>();
        if (PlayerRigidbody == null)
        {
            Debug.LogError("Player is missing a Rigidbody component");
        }
    }

    
    
    void Update()
    {
        MovePlayer();
        Shoot();
    }

    private void MovePlayer()   // Gets the input from the unity menu and makes the player move times the SpaceshipSpeed.
    {
        var horizontalInput = Input.GetAxisRaw("Horizontal");
        var verticalInput = Input.GetAxisRaw("Vertical");

        PlayerRigidbody.velocity = new Vector2(horizontalInput * GameSettings.SpaceshipSpeed, verticalInput * GameSettings.SpaceshipSpeed);
    }

    private void Shoot()    // Gets the input from the unity menu and makes the player fire.
    {
        if (Input.GetButton("Fire1") && Time.time > nextFire)
            {
                nextFire = Time.time + GameSettings.ReloadSpeed / 10;
                Instantiate(Projectile, transform.position, Quaternion.identity);
            }
    }
}
