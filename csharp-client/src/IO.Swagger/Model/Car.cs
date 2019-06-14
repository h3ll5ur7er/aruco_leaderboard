/* 
 * API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// Car
    /// </summary>
    [DataContract]
    public partial class Car :  IEquatable<Car>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Car" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="marker1">marker1.</param>
        /// <param name="marker2">marker2.</param>
        /// <param name="marker3">marker3.</param>
        /// <param name="marker4">marker4.</param>
        /// <param name="driverId">driverId.</param>
        /// <param name="teamId">teamId.</param>
        /// <param name="categoryId">categoryId.</param>
        public Car(int? id = default(int?), int? marker1 = default(int?), int? marker2 = default(int?), int? marker3 = default(int?), int? marker4 = default(int?), int? driverId = default(int?), int? teamId = default(int?), int? categoryId = default(int?))
        {
            this.Id = id;
            this.Marker1 = marker1;
            this.Marker2 = marker2;
            this.Marker3 = marker3;
            this.Marker4 = marker4;
            this.DriverId = driverId;
            this.TeamId = teamId;
            this.CategoryId = categoryId;
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public int? Id { get; set; }

        /// <summary>
        /// Gets or Sets Marker1
        /// </summary>
        [DataMember(Name="marker1", EmitDefaultValue=false)]
        public int? Marker1 { get; set; }

        /// <summary>
        /// Gets or Sets Marker2
        /// </summary>
        [DataMember(Name="marker2", EmitDefaultValue=false)]
        public int? Marker2 { get; set; }

        /// <summary>
        /// Gets or Sets Marker3
        /// </summary>
        [DataMember(Name="marker3", EmitDefaultValue=false)]
        public int? Marker3 { get; set; }

        /// <summary>
        /// Gets or Sets Marker4
        /// </summary>
        [DataMember(Name="marker4", EmitDefaultValue=false)]
        public int? Marker4 { get; set; }

        /// <summary>
        /// Gets or Sets DriverId
        /// </summary>
        [DataMember(Name="driver_id", EmitDefaultValue=false)]
        public int? DriverId { get; set; }

        /// <summary>
        /// Gets or Sets TeamId
        /// </summary>
        [DataMember(Name="team_id", EmitDefaultValue=false)]
        public int? TeamId { get; set; }

        /// <summary>
        /// Gets or Sets CategoryId
        /// </summary>
        [DataMember(Name="category_id", EmitDefaultValue=false)]
        public int? CategoryId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Car {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Marker1: ").Append(Marker1).Append("\n");
            sb.Append("  Marker2: ").Append(Marker2).Append("\n");
            sb.Append("  Marker3: ").Append(Marker3).Append("\n");
            sb.Append("  Marker4: ").Append(Marker4).Append("\n");
            sb.Append("  DriverId: ").Append(DriverId).Append("\n");
            sb.Append("  TeamId: ").Append(TeamId).Append("\n");
            sb.Append("  CategoryId: ").Append(CategoryId).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as Car);
        }

        /// <summary>
        /// Returns true if Car instances are equal
        /// </summary>
        /// <param name="input">Instance of Car to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Car input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.Marker1 == input.Marker1 ||
                    (this.Marker1 != null &&
                    this.Marker1.Equals(input.Marker1))
                ) && 
                (
                    this.Marker2 == input.Marker2 ||
                    (this.Marker2 != null &&
                    this.Marker2.Equals(input.Marker2))
                ) && 
                (
                    this.Marker3 == input.Marker3 ||
                    (this.Marker3 != null &&
                    this.Marker3.Equals(input.Marker3))
                ) && 
                (
                    this.Marker4 == input.Marker4 ||
                    (this.Marker4 != null &&
                    this.Marker4.Equals(input.Marker4))
                ) && 
                (
                    this.DriverId == input.DriverId ||
                    (this.DriverId != null &&
                    this.DriverId.Equals(input.DriverId))
                ) && 
                (
                    this.TeamId == input.TeamId ||
                    (this.TeamId != null &&
                    this.TeamId.Equals(input.TeamId))
                ) && 
                (
                    this.CategoryId == input.CategoryId ||
                    (this.CategoryId != null &&
                    this.CategoryId.Equals(input.CategoryId))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.Marker1 != null)
                    hashCode = hashCode * 59 + this.Marker1.GetHashCode();
                if (this.Marker2 != null)
                    hashCode = hashCode * 59 + this.Marker2.GetHashCode();
                if (this.Marker3 != null)
                    hashCode = hashCode * 59 + this.Marker3.GetHashCode();
                if (this.Marker4 != null)
                    hashCode = hashCode * 59 + this.Marker4.GetHashCode();
                if (this.DriverId != null)
                    hashCode = hashCode * 59 + this.DriverId.GetHashCode();
                if (this.TeamId != null)
                    hashCode = hashCode * 59 + this.TeamId.GetHashCode();
                if (this.CategoryId != null)
                    hashCode = hashCode * 59 + this.CategoryId.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}