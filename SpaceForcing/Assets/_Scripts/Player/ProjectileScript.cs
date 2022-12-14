using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*  
    ####################################################
    #               ProjectileScript.cs                #
    #--------------------------------------------------#
    # This script moves the projectile to the right.   #
    #                                                  #
    # Speed is given in: GameSettings.cs               #
    ####################################################
*/  
public class ProjectileScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;

    private Rigidbody2D ProjectileRigidbody;


    void Start()    // Gets the rigidbody of the projectile
    {
        ProjectileRigidbody = GetComponent<Rigidbody2D>();
        if (ProjectileRigidbody == null)
        {
            Debug.LogError("Projectile is missing a Rigidbody component");
        }
    }

    
    void Update()
    {
        MoveBullet();
    }

    private void MoveBullet()   // Makes a temp vecotor that will be added to the current positon of the projectile. "* Time.deltaTime" makes it so that it it frames(10 frames per ProjectileSpeed)
    {
        Vector3 tempVect = new Vector3(1, 0, 0);
        tempVect = tempVect.normalized * GameSettings.ProjectileSpeed * Time.deltaTime * 10;

        ProjectileRigidbody.MovePosition(transform.position + tempVect);
    }

    void OnBecameInvisible() // Destroys the object when off screen.
    {
        Destroy(gameObject);
    }


}
