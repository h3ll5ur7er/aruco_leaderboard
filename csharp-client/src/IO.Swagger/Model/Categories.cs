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
    /// Categories
    /// </summary>
    [DataContract]
    public partial class Categories :  IEquatable<Categories>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Categories" /> class.
        /// </summary>
        /// <param name="categories">categories.</param>
        public Categories(List<Category> categories = default(List<Category>))
        {
            this._Categories = categories;
        }
        
        /// <summary>
        /// Gets or Sets _Categories
        /// </summary>
        [DataMember(Name="categories", EmitDefaultValue=false)]
        public List<Category> _Categories { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Categories {\n");
            sb.Append("  _Categories: ").Append(_Categories).Append("\n");
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
            return this.Equals(input as Categories);
        }

        /// <summary>
        /// Returns true if Categories instances are equal
        /// </summary>
        /// <param name="input">Instance of Categories to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Categories input)
        {
            if (input == null)
                return false;

            return 
                (
                    this._Categories == input._Categories ||
                    this._Categories != null &&
                    this._Categories.SequenceEqual(input._Categories)
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
                if (this._Categories != null)
                    hashCode = hashCode * 59 + this._Categories.GetHashCode();
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
